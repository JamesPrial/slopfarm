# Claude Code Slash Commands

This directory contains custom slash commands for Claude Code that enhance development workflow.

## Available Commands

### `/implement`
Systematically implement features or fixes following best practices:
- Plans the implementation approach
- Explores the codebase to understand context
- Writes focused, minimal code changes
- Ensures security and quality standards

### `/plan`
Create detailed implementation plans before writing code:
- Analyzes requirements thoroughly
- Explores architecture and patterns
- Designs solution with step-by-step approach
- Identifies risks and alternatives

### `/review`
Comprehensive code review of recent changes:
- Checks correctness and security
- Evaluates code quality and consistency
- Assesses test coverage
- Provides constructive feedback

### `/test`
Run and analyze project tests:
- Executes test suites
- Analyzes failures and their root causes
- Fixes issues in code or tests
- Ensures reliable test coverage

## Usage

Simply type the slash command in your conversation with Claude Code:

```
/implement Add user authentication to the API
```

```
/plan Design a caching layer for the database
```

```
/review
```

```
/test
```

## Customization

You can modify these commands or add new ones by creating `.md` files in this directory. Each file becomes a slash command that injects its content as a prompt.

## Learn More

Visit the [Claude Code documentation](https://github.com/anthropics/claude-code) for more information on slash commands and customization.
