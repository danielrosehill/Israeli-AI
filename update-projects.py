#!/usr/bin/env python3
"""
Update script for Israel-Related MCPs project index.
Fetches latest information from GitHub repositories and updates projects.json.
"""

import json
import requests
import sys
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


def fetch_github_repo_info(repo_url: str) -> Optional[Dict]:
    """
    Fetch repository information from GitHub API.

    Args:
        repo_url: Full GitHub repository URL

    Returns:
        Dictionary with repo info or None if failed
    """
    # Extract owner and repo name from URL
    parts = repo_url.rstrip('/').split('/')
    if len(parts) < 2:
        return None

    owner = parts[-2]
    repo = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "description": data.get("description", ""),
            "language": data.get("language", "unknown").lower() if data.get("language") else "unknown",
            "stars": data.get("stargazers_count", 0),
            "last_updated": data.get("updated_at", ""),
            "topics": data.get("topics", []),
            "homepage": data.get("homepage", "")
        }
    except Exception as e:
        print(f"Error fetching {repo_url}: {e}", file=sys.stderr)
        return None


def update_project_from_github(project: Dict) -> Dict:
    """
    Update a project entry with latest GitHub information.

    Args:
        project: Project dictionary

    Returns:
        Updated project dictionary
    """
    repo_url = project.get("repository")
    if not repo_url:
        return project

    print(f"Updating {project['name']}...")

    github_info = fetch_github_repo_info(repo_url)
    if not github_info:
        return project

    # Update language if it was unknown
    if project.get("language") == "unknown" and github_info["language"] != "unknown":
        project["language"] = github_info["language"]

    # Add GitHub metadata
    project["github_stars"] = github_info["stars"]
    project["github_topics"] = github_info["topics"]

    if github_info["homepage"]:
        project["homepage"] = github_info["homepage"]

    return project


def update_projects_json(filepath: Path, fetch_github: bool = False):
    """
    Update the projects.json file.

    Args:
        filepath: Path to projects.json
        fetch_github: Whether to fetch latest info from GitHub API
    """
    # Load existing data
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update metadata
    data["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    data["metadata"]["total_projects"] = len(data["projects"])

    # Optionally fetch GitHub info
    if fetch_github:
        print("Fetching latest information from GitHub...")
        for i, project in enumerate(data["projects"]):
            data["projects"][i] = update_project_from_github(project)

    # Save updated data
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Updated {filepath}")
    print(f"  Total projects: {data['metadata']['total_projects']}")
    print(f"  Last updated: {data['metadata']['last_updated']}")


def add_project(filepath: Path, repo_url: str, category: str, description: str = ""):
    """
    Add a new project to the index.

    Args:
        filepath: Path to projects.json
        repo_url: GitHub repository URL
        category: Project category
        description: Optional description override
    """
    # Load existing data
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract repo info
    parts = repo_url.rstrip('/').split('/')
    author = parts[-2]
    repo_name = parts[-1]

    # Create project ID
    project_id = repo_name.lower().replace('_', '-')

    # Check if already exists
    if any(p["id"] == project_id for p in data["projects"]):
        print(f"Project {project_id} already exists!")
        return

    # Fetch GitHub info
    github_info = fetch_github_repo_info(repo_url)

    # Create new project entry
    new_project = {
        "id": project_id,
        "name": repo_name.replace('-', ' ').replace('_', ' ').title(),
        "repository": repo_url,
        "author": author,
        "author_url": f"https://github.com/{author}",
        "category": category,
        "description": description or (github_info["description"] if github_info else ""),
        "features": [],
        "data_sources": [],
        "language": github_info["language"] if github_info else "unknown",
        "status": "active"
    }

    if github_info:
        new_project["github_stars"] = github_info["stars"]
        new_project["github_topics"] = github_info["topics"]

    # Add to projects list
    data["projects"].append(new_project)

    # Update metadata
    data["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    data["metadata"]["total_projects"] = len(data["projects"])

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✓ Added {new_project['name']}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Manage Israel-Related MCPs project index")
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update metadata and optionally fetch from GitHub"
    )
    parser.add_argument(
        "--fetch-github",
        action="store_true",
        help="Fetch latest information from GitHub API"
    )
    parser.add_argument(
        "--add",
        metavar="REPO_URL",
        help="Add a new project by GitHub URL"
    )
    parser.add_argument(
        "--category",
        help="Category for new project (required with --add)"
    )
    parser.add_argument(
        "--description",
        help="Description for new project (optional with --add)"
    )

    args = parser.parse_args()

    filepath = Path(__file__).parent / "projects.json"

    if args.add:
        if not args.category:
            print("Error: --category is required when adding a project", file=sys.stderr)
            sys.exit(1)
        add_project(filepath, args.add, args.category, args.description or "")
    elif args.update or args.fetch_github:
        update_projects_json(filepath, fetch_github=args.fetch_github)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
