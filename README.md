# Python

This repository holds the most interesting solutions, exercises, homeworks done in Python language since I've been studying at some massive programming courses provided at the educational online platforms such as GeekBrains, Yandex Academy, etc.

## Conventional commits

All commits must adhere to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) spec.

Most of the commit types originally from:
* [Angular Git Commit Message Conventions](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#type)
* [commitizen/cz-conventional-changelog](https://github.com/commitizen/cz-conventional-changelog)
* [conventional-commit-types](https://github.com/commitizen/conventional-commit-types)

## Commit types

| Commit Type | Title                     | Description                                                                                                 |
| ----------- | ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `chore`     | Chores                    | Changes that don't modify src or test files                                                                 |
| `ci`        | Continuous Integrations   | Changes to CI configuration files and scripts                                                               |
| `dc`        | Driver Code / Driver Class| A driver code or class that drives the execution of the overall task                                        |
| `docs`      | Documentation             | Documentation only changes                                                                                  |
| `feat`      | Features                  | A new feature                                                                                               |
| `fix`       | Bug Fixes                 | A bug fix                                                                                                   |
| `perf`      | Performance Improvements  | A code change that improves performance                                                                     |
| `refactor`  | Code Refactoring          | A code change that neither fixes a bug nor adds a feature                                                   |
| `build`     | Builds                    | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)         |
| `revert`    | Reverts                   | Reverts a previous commit                                                                                   |
| `style`     | Styles                    | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)      |
| `test`      | Tests                     | Adding missing tests or correcting existing tests                                                           |
| `theme`     | Themes                    | Changes related to UI theming                                                                               |

When adding a new file to the Git repository none of the above commit types is used.

## Conventions

### Naming of Branches

Branch identifiers must adhere to the format `type/description-of-the-change`.

*Type* must fall into one of the following categories:

* `chore` for modifications not linked to the Kotlin source code, such as alterations in the build configuration
* `doc` for modifications concerning source code documentation, or external documents like the README
* `feat` for introducing a new feature to the app
* `fix` for rectifying bugs
* `refactor` for enhancing one or more units of code, without affecting the app's behaviour
* `test` for all test-related activities (adding a new test suite, introducing a new test into an existing test suite, or improving/modifying the performance or behaviour of an existing test)

_description of change_ must be a succinct and significant depiction of the expected change outcome; words should be separated by a dash `-`

The entire branch name must be in lower case.

### Commit Message Format

The prescribed format for a commit message is as follows:

```
<Title of the commit>

#comment <Description of the changes>
Affected: <List of affected classes or behaviours>
```

_Title_ is mandatory and must begin with a capital letter.

`#comment` field is optional if the Title can comprehensively describe the changes, otherwise, it is mandatory. The body of the comment must start with a capital letter.

`Affected` is optional and must be a comma-separated list of the elements impacted by the changes, it could be the name of a class or a behaviour.

To ensure consistency and clarity, it's recommended to use the following template when creating your commit messages:

```bash
git commit -m "<Type>: <Title of the commit>" -m "#comment <Description of the changes>" -m "Affected: <List of affected classes or behaviours>"
```

In this template:

* `<Type>`: This is the type of commit, such as feat, fix, docs, etc.
* `<Title of the commit>`: This is a brief, clear summary of the changes the commit introduces.
* `<Description of the changes>`: This is a more detailed explanation of what changes the commit introduces.
* `<List of affected classes or behaviours>`: This is a list of classes or behaviours that are affected by the changes introduced in the commit.
