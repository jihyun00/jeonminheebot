#!/bin/sh


echo "flake8..."

flake8 .

echo "import-order..."

import-order jeonminheebot .
