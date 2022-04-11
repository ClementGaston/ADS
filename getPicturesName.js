const path = require('path');
const fs = require('fs');

fs.readdir(
    path.resolve(__dirname, './images'),
    (err, files) => {
        if (err) throw err;
        
        files.map((file) => {
            if(file.slice(-4) === '.jpg') {
                nameFile = file.slice(0, -4);

                // console.log(`<img src="./resizedImages/${nameFile}_3x.jpg" alt="${nameFile}" />`)
                console.log(`<img srcset="./resizedImages/${nameFile}_1x.jpg 480w, ./resizedImages/${nameFile}_2x.jpg 960w" alt="${nameFile}" />`)
            }
        })
    }
);