
Shad4FastHtml now uses the Tailwind CSS standalone package by default, replacing the CDN version. This change allows for minification and bundling of used styles, optimizing the bundle size for production.

> **Note:** To use the CDN instead, set the `tw_link` parameter to `True` in the `ShadHead` function.

For more information on getting started with the standalone package, check out this <a href="https://tailwindcss.com/blog/standalone-cli" target="_blank">Tailwind CSS blog post</a>.

> **Important:** Work is in progress to split the code into smaller, more modular components. A PyPi package solution is also being developed, which will include scripts for easy setup and usage.

## Setup Instructions

1. **Install Tailwind CSS:** Download and install the standalone Tailwind CSS packagefor your operating system from <a href="https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.10" target="_blank">here</a>, or follow the blog post guide above to install it via the CLI.

2. **Configure Permissions:** Run CLI commands to give Tailwind CSS executable permissions. (Optional: Rename the package for ease of use)

3. **Project Structure:** Copy `globals.css` and `tailwind.config.js` into your project root. Your structure should look like this:

   ```shell
   .
   ├── globals.css
   ├── main.py
   ├── tailwind.config.js
   └── tailwindcss
   ```

4. **Configure Content:** Update the `content` section in `tailwind.config.js` to include files with Tailwind classes:

   ```javascript
   content: ["./**/*.py", "./docs/**/*.py"],
   ```

5. **Development Mode:** Run the Tailwind CLI to watch for changes and generate `output.css`:

   ```bash
   ./tailwindcss -i globals.css -o output.css --watch
   ```

6. **Production Build:** Minify the `output.css` file for deployment:

   ```bash
   ./tailwindcss -i globals.css -o output.css --minify
   ```

> **Note:** Include a link to `output.css` in your HTML:
> ```html
> <link rel="stylesheet" href="output.css">
> ```
> Adjust the `href` path if necessary for different directory structures.

## Configuration Options

- **Theme Customization:** Modify `globals.css` and `tailwind.config.js` to configure Tailwind and Shadcn themes. Refer to the <a href="https://ui.shadcn.com/docs/installation/manual" target="_blank"> Shadcn documentation</a> for a detailed reference.

- **Plugins:** Default Tailwind plugins are included in the standalone package. You can import them in `tailwind.config.js` as shown below:

  ```javascript
  plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/container-queries'),
  ],
  ```

> **Note:** Support for third-party plugins is currently in development.

---
