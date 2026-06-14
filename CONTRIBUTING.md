# Contributing Guidelines

We welcome contributions to AskDocs! This document outlines the process for contributing to the project and helps ensure that all contributions are consistent, high-quality, and aligned with the project's goals.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Issues](#reporting-issues)
- [Development Workflow](#development-workflow)
- [Pull Request Submission](#pull-request-submission)
- [Code Review Process](#code-review-process)
- [Code Style Guidelines](#code-style-guidelines)
- [License](#license)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- Be respectful and inclusive of all contributors
- Welcome constructive feedback and criticism
- Focus on what's best for the community and the project
- Show empathy towards other contributors
- Avoid using offensive or inappropriate language

## How Can I Contribute?

There are many ways to contribute to AskDocs:

- Reporting bugs and issues
- Suggesting new features or improvements
- Writing documentation
- Submitting code changes or fixes
- Reviewing pull requests
- Helping other users in discussions

## Reporting Issues

If you encounter a bug or have a feature request, please open an issue in the project repository. When reporting an issue, please include:

### Bug Reports
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment details (Python version, OS, etc.)
- Any error messages you received

### Feature Requests
- A clear, descriptive title
- A detailed description of the feature you'd like to see
- Why you think this feature would be valuable
- Any implementation ideas you have

## Development Workflow

Follow these steps to set up your development environment and contribute code:

### 1. Fork the Repository
- Create a personal fork of the project on GitHub
- Clone your fork to your local machine

### 2. Set Up Your Development Environment

#### Prerequisites
- Python 3.9 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))

#### Installation Steps
```powershell
# Clone your forked repository
git clone https://github.com/your-username/askdocs.git
cd askdocs

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Create a .env file in the project root directory with your API key:
# GROQ_API_KEY=your_groq_api_key_here
```

### 3. Create a Feature Branch
Always create a new branch for your work. Use a descriptive name that follows our branch naming conventions:

```powershell
git checkout -b <branch-type>/<descriptive-name>
```

#### Branch Naming Conventions
- `feature/`: For new features (e.g., `feature/multi-document-support`)
- `fix/`: For bug fixes (e.g., `fix/pdf-upload-error`)
- `docs/`: For documentation changes (e.g., `docs/update-readme`)
- `refactor/`: For code refactoring (e.g., `refactor/improve-error-handling`)
- `test/`: For adding or updating tests (e.g., `test/add-unit-tests`)

### 4. Make Your Changes
- Follow our [Code Style Guidelines](#code-style-guidelines)
- Keep your changes focused and atomic
- Test your changes thoroughly
- Update documentation if necessary
- Add comments where appropriate

### 5. Test Your Changes
Run the application and verify that your changes work correctly:
```powershell
streamlit run app.py
```
The application will start and automatically open in your default browser at `http://localhost:8501`.

### 6. Commit Your Changes
Write clear, descriptive commit messages:
```powershell
git add .
git commit -m "Add: Descriptive commit message"
```

#### Commit Message Guidelines
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Fix bug" not "Fixes bug")
- Keep messages concise but descriptive
- Reference issue numbers when applicable (e.g., "Fix: PDF upload error #42")

### 7. Push to Your Branch
```powershell
git push origin <your-branch-name>
```

### 8. Open a Pull Request
Once your changes are ready, open a pull request from your branch to the main repository's main branch.

## Pull Request Submission

When submitting a pull request, please:

1. **Fill out the PR Template**: Provide a clear description of your changes
2. **Link Related Issues**: Reference any issues your PR addresses
3. **Ensure Tests Pass**: Verify that your changes don't break existing functionality
4. **Keep PRs Focused**: Each PR should address one specific issue or feature
5. **Update Documentation**: If your changes affect documentation, update it accordingly

### Pull Request Checklist
- [ ] I have read the Contributing Guidelines
- [ ] My code follows the project's style guidelines
- [ ] I have tested my changes thoroughly
- [ ] I have updated the documentation (if necessary)
- [ ] My commit messages are clear and descriptive

## Code Review Process

All pull requests will be reviewed by project maintainers. During the review process:

1. A maintainer will review your code
2. They may request changes or ask questions
3. Address any feedback and push updates to your branch
4. Once approved, your PR will be merged

## Code Style Guidelines

To maintain consistency across the codebase, please follow these guidelines:

### Python Code
- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Add docstrings for public functions and classes
- Use type hints where appropriate

### General Guidelines
- Keep code clean and readable
- Remove any unnecessary comments or debug code
- Avoid code duplication
- Write modular, reusable code

## License

By contributing to AskDocs, you agree that your contributions will be licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
