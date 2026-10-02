# On Windows (PowerShell):
@"
# Git Workflow Lab

A simple Python project demonstrating Git workflow best practices including branching, pull requests, and tagging.

## Overview

This project contains a basic "hello world" application showcasing:
- Feature branch development
- Pull request workflow
- Version tagging
- Collaborative development practices

## Installation

\`\`\`bash
python hello.py
\`\`\`

## Features

- Simple greeting functionality
- Extensible design for adding more features

## Contributing

See CONTRIBUTORS.md for a list of contributors to this project.

## Version

Current version: v1.0.0
"@ | Out-File README.md -Encoding utf8

# On Mac/Linux:
cat > README.md << 'EOF'
# Git Workflow Lab

A simple Python project demonstrating Git workflow best practices including branching, pull requests, and tagging.

## Overview

This project contains a basic "hello world" application showcasing:
- Feature branch development
- Pull request workflow
- Version tagging
- Collaborative development practices

## Installation

```bash
python hello.py
```

## Features

- Simple greeting functionality
- Extensible design for adding more features

## Contributing

See CONTRIBUTORS.md for a list of contributors to this project.

## Version

Current version: v1.0.0
EOF