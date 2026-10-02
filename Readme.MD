# Git Workflow Lab

A simple Python project demonstrating Git workflow best practices including branching, pull requests, and tagging.

## Installation

### Prerequisites

Before running this project, you need to install Git and Python.

#### Install Git

**Windows:**
1. Download Git from [git-scm.com](https://git-scm.com)
2. Run the installer and follow the setup wizard
3. Choose default options or customize as needed
4. Verify installation:
```bash
   git --version
```

**Mac:**
1. Install via Homebrew:
```bash
   brew install git
```
2. Or download from [git-scm.com](https://git-scm.com)
3. Verify installation:
```bash
   git --version
```

**Linux:**
1. Install via package manager:
```bash
   # Ubuntu/Debian
   sudo apt-get install git
   
   # Fedora
   sudo dnf install git
```
2. Verify installation:
```bash
   git --version
```

### Configure Git

After installing Git, configure your user information:

```bash
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"
```

### Run the Application

```bash
python hello.py
```

## Features

- Simple greeting functionality
- Multiple greeting options (formal and casual)
- Extensible design for adding more features

## Contributing

See CONTRIBUTORS.md for a list of contributors to this project.

## Version

Current version: v1.0.0.