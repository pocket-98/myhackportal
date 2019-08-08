#!/bin/bash
echo dl bootstrap css
curl -Lo ncsu-bootstrap.min.css "https://cdn.ncsu.edu/brand-assets/bootstrap/css/bootstrap.css"

echo dl bootstrap js
curl -Lo ncsu-bootstrap.min.js "https://cdn.ncsu.edu/brand-assets/bootstrap/js/bootstrap.min.js"

echo dl ncsu fonts
curl -Lo ncsu-font.css "https://cdn.ncsu.edu/brand-assets/fonts/include.css"

echo dl ncsu util bar
curl -Lo ncsu-utilbar.min.js "https://cdn.ncsu.edu/brand-assets/utility-bar/ub.php"
sed -i "s/ub\.php/ncsu-utilbar\.min\.js/" ncsu-utilbar.min.js
