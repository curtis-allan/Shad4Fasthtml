*This documentation is a work in progress. I appreciate your patience and feedback as I continue to build upon the repo. All credits go to <a href="https://x.com/shadcn" target="_blank">@Shadcn</a> for the component styles and <a href="https://x.com/jeremyphoward" target="_blank">@JeremyPHoward</a> for the fastHtml framework.*

## Quick Start Guide

### Setup & Installation

Getting started with Shadcn UI for FastHTML is quick and easy. Follow these simple steps to set up your project:

1. Copy the `shadcn.py` file from the GitHub repository into your FastHTML project directory.

   > **Note:** A pip module will be available in the near future. This is a temporary solution.

2. Add the following import statements to the top of the file where you want to use the components:

   ```python
   from fasthtml import *
   from shadcn import *
   ```

3. Include the Shadcn headers in your FastHTML headers and disable the default Pico.css header, as shown below:

   ```python
   app, rt = fast_app(
       pico=False,
       hdrs=(ShadHead(),),
   )
   ```

### Configuration

#### Tailwind Configuration

Shadcn-ui components use TailwindCSS for styling by default. Shad4FastHtml now uses the Tailwind CSS standalone package by default, replacing the CDN version. This change allows for minification and bundling of used styles, optimizing the bundle size for production.

If you wish to use the CDN instead, set the `tw_link` parameter to `True` in the `ShadHead` function. See the <a hx-boost="true" href="/getting-started/tailwind-setup">Tailwind Setup Guide</a> for more information.

#### Lucide Icons

As a preference, I have chosen to use Lucide icons for the project. If you wish to use another icon library or wish to ommit the lucide import and script elements, you can do so by setting the `lucide_link` parameter to `False` in the `ShadHead` function.

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(lucid=False),),
)
```

### You're All Set!

Congratulations! You've successfully set up Shadcn UI for your FastHTML project. You're now ready to start using the UI components in your app.

## Using Components

To implement Shadcn UI components in your codebase, refer to the relevant component documentation. Each component has its own set of properties and usage guidelines.

## Known Issuess

* Using Lucide via the cdn results in icon flickering on page load.

* Toast: Client side render + mobile touch handling + disable scroll while hovering.

* Add assetions for all required parameters.

* Table demo - theme toggle fix

* Documentation fixing and cleaning up

## Need Help?

If you encounter any issues or have questions, please open an issue on the GitHub repository and either myself or a member of the community will try to help.