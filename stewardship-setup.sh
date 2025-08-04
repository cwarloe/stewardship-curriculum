#!/usr/bin/env bash
# stewardship-setup.sh
# Usage: bash stewardship-setup.sh

# Configuration (update as needed)
GITHUB_ORG_OR_USER="your-github-username-or-org"
REPO_NAME="stewardship-curriculum"
DESCRIPTION="Stewardship curriculum repo"

set -euo pipefail

echo "Creating GitHub repository..."
gh repo create "$GITHUB_ORG_OR_USER/$REPO_NAME" --public --description "$DESCRIPTION" --source=. --remote=origin

echo "Initializing local repo..."
git init
git checkout -b main

echo "Committing initial files..."
git add .
git commit -m "Initial commit: curriculum structure"

echo "Pushing to GitHub..."
git push -u origin main

echo "Done!"
