*This documentation is a work in progress. I appreciate your patience and feedback as I continue to build upon the repo. All credits go to <a href="https://x.com/shadcn" target="_blank">@Shadcn</a> for the component styles and <a href="https://x.com/jeremyphoward" target="_blank">@JeremyPHoward</a> for the fastHtml framework.*

[![PyPI - Version](https://img.shields.io/pypi/v/shad4fast.svg)](https://pypi.org/project/shad4fast)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/shad4fast.svg)](https://pypi.org/project/shad4fast)

## Quick Start Guide

### Setup & Installation

Getting started with Shadcn UI for FastHTML is quick and easy. Follow these steps to set up your project:

1. Install the `Shad4Fast` pip package. This can be used to initialize a new project too, all dependencies (including FastHtml) will be installed:

```zsh
pip install shad4fast
```

2. Add the following import statement to the top of the file where you want to use the components:

```python
from fasthtml import FastHtml, serve
from shad4fast import * # Or individual components: Button, Input etc.
```

>[!NOTE]
> If importing components individually, make sure to also import the `ShadHead()` function.

3. Include `ShadHead()` in your FastHTML headers and disable the default Pico.css header, as shown below:

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(),),
)
```

### Configuration

#### Tailwind Configuration

As with Shadcn-ui components, Shad4Fast uses `TailwindCSS` styles by default. This can be setup in two ways: via a cdn script or the tailwind <a href="https://tailwindcss.com/blog/standalone-cli" target="_blank">standalone package</a>. 

Shad4Fast provides in-built functionality for both of these use cases. For a detailed documentation, refer to the <a target="_blank" href="https://shad4fasthtml.com/getting-started/tailwind-setup">Tailwind Setup</a> guide.

The easiest way to get started is to simply set the `tw_cdn` option within the ShadHead function to `True`:

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(tw_cdn=True),),
)
```

#### Theme Handling

Included in the Shad4Fast package is a script to streamline the use of light/dark themes within your FastHtml application. This can be used by setting the `theme_handle` attribute to `True` as shown below:

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(tw_cdn=True, theme_handle=True),),
)
```

Setting this to `True` includes a script in the headers that allows for toggling of the current theme based on standard light/ dark mode determination. For a full guide on how this works and setting up a theme toggle button, see the <a href="https://shad4fasthtml.com/getting-started/theme-configuration" target="_blank">Theme Configuration</a> guide.


### You're All Set!

Congratulations! You've successfully set up Shad4FastHtml for your project! You're now ready to start using the UI components in your app.

>[!IMPORTANT]
> This project is still in its youth. If you encounter any bugs or issues, please open an issue on the GitHub repository.

## Using Components

To implement Shadcn UI components in your codebase, refer to the relevant component documentation. Each component has its own set of properties and usage guidelines.

## Lucide Icons

Shad4FastHtml relies on <a href="https://lucide.dev/icons/" target="_blank">Lucide Icons</a> as a dependency. This was optional in the previous versions, however certain components require Lucide icons to accurately portray their Shadcn counterpart. 

To improve the usage of these icons within FastHtml, I create a pip package called `lucide-fasthtml` to improve the rendering and configuration of the icons. This is set as a dependency for `Shad4Fast` and will be automatically installed and setup upon installing Shad4Fast, however the package can be used purely with FastHtml alone. 

As a general overview, the `lucide-fasthtml` package provides a `Lucide` component that takes a valid lucide icon name and renders the icon. A set of background functions handle the fetching of the svg data and save it to an `icons.py` file generated at the root of your project.

 For a full reference on the package and its usage, refer to the github repo <a href="https://github.com/curtis-allan/lucide-fasthtml" target="_blank">here.</a>

## Roadmap

* **IN PROGRESS**: Documentation fixing and cleaning up.

* Implement all existing Shadcn-ui components.

* Add type assertions for all component attributes, with proper error handling and documentation.

* Complete aria attributes for all components. Enhance and optimize the JS implementation.

* Future plan:
    * Streamline the use of V0 with the framework to allow for fully-generative UI frameworks for FastHtml.

## Need Help?

If you encounter any issues or have questions, please reach out either through the <a href="https://github.com/curtis-allan/shadcn-fasthtml-framework" target="_blank">Github</a> repo or send me a dm on <a href="https://x.com/CurtisJAllan" target="_blank">X aka twitter</a> and either myself or a member of the community will try to help out.
