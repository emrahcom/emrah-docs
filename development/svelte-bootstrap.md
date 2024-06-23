# Svelte and Bootstap

## Packages

```bash
yarn add @popperjs/core
yarn add bootstrap
yarn add bootstrap-icons
yarn add -D @types/bootstrap
```

## layout.svelte

```javascript
  import "bootstrap-icons/font/bootstrap-icons.css";
  import "bootstrap/dist/css/bootstrap.min.css";
  import "bootstrap/dist/js/bootstrap.bundle.min.js";
```

## Tooltip

```javascript
  import { Tooltip } from "bootstrap";
  import { onMount } from "svelte";

  onMount(() => {
    const elementsWithTooltip = document.querySelectorAll(
      '[data-bs-toggle="tooltip"]',
    );

    [...elementsWithTooltip].map((el) => new Tooltip(el));
  });
```
