# On Windows (PowerShell):
@"
# Contributors

This project is built by the following contributors:

- Your Name - Project initiator and maintainer

## How to Contribute

If you'd like to contribute to this project:

1. Fork the repository
2. Create a feature branch (\`git checkout -b feature/your-feature\`)
3. Make your changes
4. Commit your changes (\`git commit -m 'Add your feature'\`)
5. Push to the branch (\`git push origin feature/your-feature\`)
6. Open a Pull Request
7. Wait for review and address feedback

Thank you for your contributions!
"@ | Out-File CONTRIBUTORS.md -Encoding utf8

# On Mac/Linux:
cat > CONTRIBUTORS.md << 'EOF'
# Contributors

This project is built by the following contributors:

- Your Name - Project initiator and maintainer

## How to Contribute

If you'd like to contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add your feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request
7. Wait for review and address feedback

Thank you for your contributions!
EOF