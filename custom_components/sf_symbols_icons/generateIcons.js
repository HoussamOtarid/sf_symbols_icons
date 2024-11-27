const fs = require('fs');
const path = require('path');

const iconsFolderPath = path.join(__dirname, 'icons');

fs.readdir(iconsFolderPath, (err, files) => {
  if (err) {
    console.error('Error reading icons folder:', err);
    return;
  }

  const icons = files
    .filter(file => file.endsWith('.svg'))
    .map(file => ({
      name: path.parse(file).name,
      file: file,
      path: `sf:${path.parse(file).name}`
    }));

  fs.writeFileSync(path.join(__dirname, 'icons.json'), JSON.stringify(icons, null, 2));

  console.log(`Generated icons.json with ${icons.length} icons.`);
});
