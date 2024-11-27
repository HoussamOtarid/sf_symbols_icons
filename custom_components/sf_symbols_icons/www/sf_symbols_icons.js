import { mdi } from 'mdi-material-design';

const iconPrefix = 'sf';

async function registerIcons() {
  try {
    const response = await fetch('/local/icons.json');
    const icons = await response.json();

    icons.forEach(icon => {
      mdi.registerIcons({
        [`${iconPrefix}:${icon.name}`]: `/local/icons/${icon.file}`
      });
    });
  } catch (error) {
    console.error("Error loading icons:", error);
  }
}

registerIcons();
