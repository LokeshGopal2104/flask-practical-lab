# Flask Templates and Jinja — Task 05

## Project Overview

This project is the fifth task in my practical Flask learning roadmap.

The objective is to understand how Flask uses Jinja templates to create dynamic HTML, perform template logic, reuse common layouts, include reusable components, transform values using filters, and create reusable template macros.

---

## Learning Objectives

- Understand Jinja templates.
- Pass variables from Flask to templates.
- Display variables using `{{ }}`.
- Use multiple template variables.
- Use conditional statements with `{% if %}`.
- Use `{% elif %}` and `{% else %}`.
- Use Jinja `for` loops.
- Use conditions inside loops.
- Use the `loop` variable.
- Use `loop.index`.
- Understand template inheritance.
- Use `{% extends %}`.
- Use `{% block %}`.
- Create reusable template components.
- Use `{% include %}`.
- Use Jinja filters.
- Use the `capitalize` filter.
- Create reusable Jinja macros.
- Pass arguments to macros.
- Understand the difference between templates, included components, and macros.

---

## Features

- Dynamic data rendered using Jinja.
- Conditional rendering based on user data.
- Iteration over a list of users.
- Numbered list using `loop.index`.
- Reusable base template.
- Reusable navigation component.
- Jinja filter for capitalization.
- Reusable user-card macro.
- Dynamic HTML generation.

---

## Project Structure

```text
05-templates-jinja/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── macros.html
│   │
│   └── components/
│       └── navbar.html
│
└── README.md