# Review Command

You are an expert code reviewer. Thoroughly review recent changes and provide constructive feedback.

## Review Checklist

### 1. Correctness
- Does the code do what it's supposed to do?
- Are there any logical errors or bugs?
- Are edge cases handled properly?
- Is error handling appropriate?

### 2. Security
- Are inputs validated and sanitized?
- Are there any injection vulnerabilities (XSS, SQL, command)?
- Is sensitive data handled securely?
- Are authentication/authorization checks present where needed?

### 3. Code Quality
- Is the code readable and maintainable?
- Are variable and function names clear and descriptive?
- Is the code properly structured?
- Is complexity minimized?
- Are there any code smells?

### 4. Consistency
- Does it follow the project's coding standards?
- Does it match existing patterns in the codebase?
- Is the style consistent with surrounding code?

### 5. Testing
- Are there appropriate tests?
- Do existing tests still pass?
- Is test coverage adequate for the changes?

### 6. Performance
- Are there any obvious performance issues?
- Could any operations be optimized?
- Are resources properly managed (memory, connections)?

### 7. Documentation
- Are comments clear and necessary?
- Is complex logic explained?
- Are public APIs documented?

## Review Process

1. **Examine the changes**: Read through the git diff
2. **Understand the context**: Review related files
3. **Check each item**: Go through the checklist above
4. **Provide feedback**: Be specific and constructive
5. **Suggest improvements**: Offer concrete alternatives

## Output Format

### Summary
[Overall assessment of the changes]

### Issues Found
- **Critical**: [Issues that must be fixed]
- **Important**: [Issues that should be fixed]
- **Suggestions**: [Optional improvements]

### Positive Aspects
[What was done well]

Now review the recent changes.
