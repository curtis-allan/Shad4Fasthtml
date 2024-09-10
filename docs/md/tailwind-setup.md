
## Setup Instructions

Shad4Fast provides two methods of integrating tailwind into your application out of the box:

1. **CDN Link** 

2. **Standalone Package**

Both methods are viable depending on your use case:

   * For development and quick iteration, the CDN is a good option. It's the easiest to implement and automatically applies styling, without any watch or build process. 

   * For production, its recommended to install the standalone package. This will reduce the bundle size considerably, as only the styles used within your project will be included.

### Using the CDN

The easiest way to get started with using Shad4Fast is via the TailwindCDN. The `Link` tag for this is pre-configured within the ShadHead() function, and can be used as shown:

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(tw_cdn=True),),
)
```

### Using the Standalone Package

This option has more of a setup/ usage overhead than the cdn, but the benefits are entirely worth it. To help streamline this, Shad4Fast includes 3 handy scripts out of the box:

| Script | Output | Function |
| --- | --- | --- |
| `shad4fast setup` | `...` | Very handy setup function. Downloads the appropriate `tailwind` package for your machine, pre-configured `globals.css` and `tailwind.config.js` files from the repo and creates a blank `output.css` file. This script acts as a boilerplate instantiator for any project using this package. |
| `shad4fast watch` | `./tailwindcss -i globals.css -o output.css --watch` | Simplifies the watch script for the tailwind package. Watches all files passed through the `tailwind.config.js` content section. |
| `shad4fast build` | `./tailwindcss -i globals.css -o output.css --minify` | Simplifies the minify script for the tailwind package. Minifies the current `output.css` file to reduce bundle size in production. |

>[!IMPORTANT]
> If you find the `watch` and `build` commands are not working correctly, adjust the `content` section within the tailwind.config.js file to point to your installation of shad4fast. You can also asjust this to point to other directories you have that include tailwind classes.

---

## Plugins

Default Tailwind plugins are included in the standalone package out of the box. If you want to use any within your project, you can simply import them in your `tailwind.config.js` file as shown below:

  ```javascript
  plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/container-queries'),
  ],
  ```

> [!NOTE] 
> Support for third-party plugins is currently unavailable. Since Shadcn's component library uses `tailwindcss-animate` for animations, the functionality is included directly in the `tailwind.config.js` file from the repo.
