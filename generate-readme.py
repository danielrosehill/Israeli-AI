#!/usr/bin/env python3
"""
Generate README.md from projects.json following Daniel's template style.
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def load_projects_data(filepath: Path) -> dict:
    """Load projects data from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_shields_badge(repo_url: str) -> str:
    """Generate shields.io badge for a GitHub repository."""
    # Extract owner/repo from URL
    parts = repo_url.rstrip('/').split('/')
    owner = parts[-2]
    repo = parts[-1]

    return f"![GitHub stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/{owner}/{repo})"


def generate_project_section(project: dict, include_notes: bool = False) -> str:
    """Generate markdown section for a single project."""
    output = []

    # Project name as heading
    output.append(f"## [{project['name']}]({project['repository']})")
    output.append("")

    # Shields.io badges
    badges = generate_shields_badge(project['repository'])
    output.append(badges)
    output.append("")

    # Description
    output.append(project['description'])
    output.append("")

    # Features (if available)
    if project.get('features') and len(project['features']) > 0:
        output.append("**Features:**")
        for feature in project['features']:
            output.append(f"- {feature}")
        output.append("")

    # Data sources
    if project.get('data_sources') and len(project['data_sources']) > 0:
        output.append(f"**Data Sources:** {', '.join(project['data_sources'])}")
        output.append("")

    # Language
    if project.get('language') and project['language'] != 'unknown':
        lang_display = project['language'].title()
        output.append(f"**Language:** {lang_display}")
        output.append("")

    # Author
    if project.get('author'):
        author_link = f"[{project['author']}]({project['author_url']})" if project.get('author_url') else project['author']
        output.append(f"**Author:** {author_link}")
        output.append("")

    # Demo link (if available)
    if project.get('demo'):
        output.append(f"**Demo:** [{project['demo']}]({project['demo']})")
        output.append("")

    # Homepage (if available)
    if project.get('homepage'):
        output.append(f"**Website:** [{project['homepage']}]({project['homepage']})")
        output.append("")

    output.append("---")
    output.append("")

    return "\n".join(output)


def generate_category_section(category_key: str, category_info: dict, projects: list) -> str:
    """Generate markdown section for a category of projects."""
    output = []

    # Category heading
    output.append(f"# {category_info['name']}")
    output.append("")
    output.append(category_info['description'])
    output.append("")

    # Projects in this category
    for project in sorted(projects, key=lambda p: p['name']):
        output.append(generate_project_section(project))

    return "\n".join(output)


def generate_toc(categories: dict, projects_by_category: dict) -> str:
    """Generate table of contents with placeholder for index."""
    output = []
    output.append("## Table of Contents")
    output.append("")
    output.append("<!-- INDEX_START -->")
    output.append("")

    for cat_key in sorted(categories.keys()):
        if cat_key == "unknown":
            continue
        cat_info = categories[cat_key]
        count = len(projects_by_category.get(cat_key, []))
        if count > 0:
            # Convert to anchor link
            anchor = cat_info['name'].lower().replace(' ', '-').replace('&', '').replace('  ', '-')
            output.append(f"- [{cat_info['name']}](#{anchor})")

    output.append("")
    output.append("<!-- INDEX_END -->")
    output.append("")
    return "\n".join(output)


def generate_authors_section(projects: list) -> str:
    """Generate alphabetical list of MCP authors."""
    output = []
    output.append("# MCP Authors")
    output.append("")
    output.append("Alphabetical list of contributors who have created Israel-related MCP servers:")
    output.append("")

    # Collect unique authors
    authors = {}
    for project in projects:
        author = project.get('author')
        author_url = project.get('author_url')
        if author and author not in authors:
            authors[author] = author_url

    # Sort alphabetically
    for author in sorted(authors.keys()):
        author_url = authors[author]
        if author_url:
            output.append(f"- [{author}]({author_url})")
        else:
            output.append(f"- {author}")

    output.append("")
    return "\n".join(output)


def generate_readme(projects_data: dict) -> str:
    """Generate complete README content."""
    output = []

    # Header
    output.append("# Israel-Related MCP Servers")
    output.append("")
    output.append("A curated list of Model Context Protocol (MCP) servers that provide access to Israeli data sources, government APIs, and services relevant to those living in or interested in Israel.")
    output.append("")

    # Group projects by category
    projects_by_category = defaultdict(list)
    for project in projects_data['projects']:
        projects_by_category[project['category']].append(project)

    # Last updated
    output.append(f"*Last updated: {projects_data['metadata']['last_updated']}*")
    output.append("")

    # Table of contents
    output.append(generate_toc(projects_data['categories'], projects_by_category))

    # Category sections
    for cat_key in sorted(projects_data['categories'].keys()):
        if cat_key == "unknown":
            continue
        projects = projects_by_category.get(cat_key, [])
        if len(projects) > 0:
            cat_info = projects_data['categories'][cat_key]
            output.append(generate_category_section(cat_key, cat_info, projects))

    # Unknown category (if any)
    if 'unknown' in projects_by_category and len(projects_by_category['unknown']) > 0:
        output.append("# Other Projects")
        output.append("")
        output.append("Projects that need categorization.")
        output.append("")
        for project in projects_by_category['unknown']:
            output.append(generate_project_section(project))

    # Authors section
    output.append(generate_authors_section(projects_data['projects']))

    # Contributing section
    output.append("# Contributing")
    output.append("")
    output.append("Anyone is welcome to open a pull request to add an Israel-related MCP server to this list.")
    output.append("")
    output.append("To add a new project:")
    output.append("1. Fork this repository")
    output.append("2. Add your project to `projects.json` using the update script:")
    output.append("   ```bash")
    output.append("   ./update-projects.py --add https://github.com/username/repo --category category-name")
    output.append("   ```")
    output.append("3. Run the README generator:")
    output.append("   ```bash")
    output.append("   ./generate-readme.py")
    output.append("   ```")
    output.append("4. Submit a pull request")
    output.append("")
    output.append("Alternatively, drop me a line at public@danielrosehill.com if you'd like me to add it manually.")
    output.append("")

    # Disclaimer
    output.append("# Disclaimer")
    output.append("")
    output.append("This resource is intended for those discovering MCP servers relevant to Israel. It is not exhaustive and is maintained on a best-effort basis.")
    output.append("")
    output.append("The inclusion of a project in this list does not constitute an endorsement. Users should evaluate each project independently for their specific use cases.")
    output.append("")

    # Footer
    output.append("---")
    output.append("")
    output.append(f"*Last updated: {projects_data['metadata']['last_updated']}*")
    output.append("")
    output.append("Maintained by [Daniel Rosehill](https://github.com/danielrosehill)")

    return "\n".join(output)


def main():
    """Main entry point."""
    # Load projects data
    projects_file = Path(__file__).parent / "projects.json"
    projects_data = load_projects_data(projects_file)

    # Generate README
    readme_content = generate_readme(projects_data)

    # Write to file
    readme_file = Path(__file__).parent / "README.md"
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"✓ Generated README.md")
    print(f"  Total projects: {projects_data['metadata']['total_projects']}")
    print(f"  Categories: {len(projects_data['categories'])}")


if __name__ == "__main__":
    main()
