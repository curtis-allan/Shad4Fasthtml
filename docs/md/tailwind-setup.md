
## ***Update!***

Shad4FastHtml now uses the Tailwind CSS standalone package by default, replacing the previous CDN import. Tailwind's play cdn, while useful for development, is not recommended for production deployments. Without a postprocessor to reduce bundle size, the cdn downloads the **entire** tailwind stylesheet into the browser, which is *big!* 

Due to this, I've been working on migrating to use the tailwind standalone package as the default for Shad4FastHtml. This change allows for minification and bundling of any used styles, optimizing the final build size for production. Outlined below are the steps to get started with the updated tailwind setup.

> [!TIP]
>To use the CDN instead, set the `tw_link` parameter to `True` in the `ShadHead` function.

For more information on getting started with the standalone package, check out this <a href="https://tailwindcss.com/blog/standalone-cli" target="_blank">Tailwind CSS blog post</a>.

Work is also in progress to split the code into smaller, more modular components. These will be available to simply `copy/paste` from the website documentations in the near future. In the meantime, the recommended way to use this library is still the current method.

> [!IMPORTANT]
>  A PyPi package solution is currently in development. This will include `CLI` scripts out of the box to simplify and streamline the setup process outlined below.

## Setup Instructions

1. **Install Tailwind CSS:** Download and install the standalone Tailwind CSS package for your operating system from <a href="https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.10" target="_blank">here</a>, or follow the blog post guide above to install it via the CLI.

2. **Configure Permissions:** Run CLI commands to give Tailwind CSS executable permissions. (Optional: Rename the package for ease of use)

3. **Project Structure:** Copy the `globals.css` and `tailwind.config.js` files from the <a href="https://github.com/curtis-allan/shadcn-fasthtml-framework" target="_blank">Github</a> repository into your project root. Your file structure should look like this:

   ```shell
   .
   ├── globals.css
   ├── main.py
   ├── tailwind.config.js
   └── tailwindcss
   ```

4. **Configure Content:** Update the `content` section in `tailwind.config.js` to include files with Tailwind classes:

   ```javascript
   content: ["./**/*.py"],
   ```

5. **Development Mode:** Run the Tailwind CLI to watch for changes and generate `output.css`:

   ```bash
   ./tailwindcss -i globals.css -o output.css --watch
   ```

>[!NOTE]
> You can choose any name for the input and output files. I chose to use `globals.css` as my input file due to familiarity from javascript development. If you do, ensure you point to the correct files when using the tailwind CLI below.

6. **Production Build:** Minify the `output.css` file for deployment:

   ```bash
   ./tailwindcss -i globals.css -o output.css --minify
   ```

> [!IMPORTANT]
> Include a link pointing to your `output.css` file or whatever name you chose:
> ```python+html
> Link(rel="stylesheet", href="output.css")
> ```
> Adjust the `href` path if necessary for different directory structures.

## Configuration Options

- **Theme Customization:** Modify `globals.css` and `tailwind.config.js` to configure Tailwind and Shadcn themes. Refer to the <a href="https://ui.shadcn.com/docs/installation/manual" target="_blank"> Shadcn documentation</a> for a detailed reference. If you're unfamiliar with Shadcn's framework, he also has a neat <a href="https://ui.shadcn.com/themes" target="_blank">theme picker</a>, allowing you to:

1. Choose a theme configuration that you like.

2. Copy the theme code and paste it into your `globals.css` file, replacing the existing css variables within `:root` and `dark`.

3. Enjoy!

- **Plugins:** Default Tailwind plugins are included in the standalone package out of the box. If you want to use any within your project, you can simply import them in your `tailwind.config.js` file as shown below:

  ```javascript
  plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/container-queries'),
  ],
  ```

> [!NOTE] 
> Support for third-party plugins is currently unavailable. I'm working on a solution for this. Since Shadcn's component library uses `tailwindcss-animate` for animations, I had to port the plugin directly into the `tailwind.config.js` file. This is a temporary solution, and I will update the documentation if i find a better solution.
