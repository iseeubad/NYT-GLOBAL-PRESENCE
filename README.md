# New York Times Global Offices Map

![NYT Global Map](https://via.placeholder.com/800x400?text=NYT+Global+Offices+Map)

An interactive visualization of The New York Times' global bureau network, showcasing the company's worldwide journalistic presence.

## Overview

This project visualizes The New York Times' global footprint, highlighting the company's headquarters in New York City alongside its extensive network of international and domestic bureaus. The interactive map provides a comprehensive view of the newspaper's global news gathering operations across 37 locations in 27 countries.

## Features

- **Interactive Map Interface:** Explore The New York Times' global presence through an intuitive map interface
- **Categorized Locations:** Distinct visual styling for headquarters, international bureaus, and US bureaus
- **Clustering:** Location markers are clustered for improved performance and visual clarity
- **Responsive Design:** Optimized for both desktop and mobile viewing
- **Layer Controls:** Toggle different bureau types on and off
- **Fullscreen Mode:** Expand the map for a more immersive viewing experience
- **Professional Styling:** Clean, branded design consistent with The New York Times visual identity

## Demo

Visit the [live demo](https://yourusername.github.io/nyt-global-map) to explore the map.

## Technologies Used

- **Python:** Core programming language
- **Folium:** Python library for creating interactive Leaflet maps
- **CartoDB Positron:** Clean, neutral base map tiles
- **Marker Clustering:** Improved performance and visual organization
- **HTML/CSS:** Custom styling for a professional appearance
- **Font Awesome:** Professional icons for location markers

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/nyt-global-map.git
cd nyt-global-map
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Generate the map:
```bash
python nyt_global_map.py
```

4. Open the generated HTML file in your web browser:
```bash
open nyt_global_offices_map.html  # On macOS
# OR
xdg-open nyt_global_offices_map.html  # On Linux
# OR
start nyt_global_offices_map.html  # On Windows
```

## Requirements

- Python 3.6+
- Folium 0.12.0+
- Web browser with JavaScript enabled

## Project Structure

```
nyt-global-map/
├── nyt_global_map.py           # Main Python script to generate the map
├── requirements.txt            # Python dependencies
├── nyt_global_offices_map.html # Generated output map
└── README.md                   # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The New York Times for their global journalistic presence
- [Folium](https://python-visualization.github.io/folium/) for the mapping library
- [CartoDB](https://carto.com/) for the base map tiles

---

*This project is for educational purposes only and is not affiliated with, endorsed by, or sponsored by The New York Times Company.*
