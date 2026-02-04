# Contributing to HydroSense

Thank you for your interest in contributing to HydroSense! This document provides guidelines for contributing to the project.

## Ways to Contribute

- Report bugs or issues
- Suggest new features or enhancements
- Add new journal sources
- Improve documentation
- Submit code improvements

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/HydroSense.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit with clear messages
7. Push to your fork
8. Submit a pull request

## Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise

## Testing

Before submitting a pull request:

1. Test with a small date range (1-2 days)
2. Verify all three tiers work correctly
3. Check that output format is valid Markdown
4. Ensure API rate limits are respected

## Pull Request Guidelines

- Provide a clear description of changes
- Reference any related issues
- Include example output if applicable
- Keep changes focused (one feature per PR)

## Adding New Journals

When adding journals to the `JOURNALS` list:

1. Verify the ISSN is correct
2. Classify as "top-tier" or "High-impact"
3. Test that papers are retrieved correctly
4. Update README.md with journal count

## Questions?

Open an issue for questions or clarifications.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
