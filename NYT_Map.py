import folium
from folium.plugins import MarkerCluster, Fullscreen

# Initialize map with a more neutral base layer and centered at a global view
m = folium.Map(location=[20, 0], zoom_start=2, control_scale=True, 
               tiles="CartoDB Positron")  # Using CartoDB Positron for a cleaner look

# Add fullscreen option
Fullscreen().add_to(m)

# Create marker clusters for better performance and visual organization
hq_cluster = MarkerCluster(name="Headquarters", overlay=True, control=False)
international_cluster = MarkerCluster(name="International Bureaus", overlay=True, control=False)
us_cluster = MarkerCluster(name="US Bureaus", overlay=True, control=False)

# Custom icons for different types of offices
hq_icon = folium.Icon(icon="building", prefix="fa", color="darkred")
intl_icon = folium.Icon(icon="newspaper", prefix="fa", color="darkblue")
us_icon = folium.Icon(icon="newspaper", prefix="fa", color="darkgreen")

# Headquarters with special styling
folium.Marker(
    location=[40.7561, -73.9903],  # 620 Eighth Avenue, NYC
    popup=folium.Popup("<b>New York Times Headquarters</b><br>620 Eighth Avenue<br>New York, NY", max_width=300),
    icon=hq_icon,
    tooltip="New York Times Headquarters"
).add_to(hq_cluster)

# International bureaus with improved data structure
international_bureaus = [
    {"name": "London", "country": "United Kingdom", "coords": [51.5074, -0.1278]},
    {"name": "Paris", "country": "France", "coords": [48.8566, 2.3522]},
    {"name": "Berlin", "country": "Germany", "coords": [52.5200, 13.4050]},
    {"name": "Rome", "country": "Italy", "coords": [41.9028, 12.4964]},
    {"name": "Brussels", "country": "Belgium", "coords": [50.8503, 4.3517]},
    {"name": "Moscow", "country": "Russia", "coords": [55.7558, 37.6173]},
    {"name": "Istanbul", "country": "Turkey", "coords": [41.0082, 28.9784]},
    {"name": "Cairo", "country": "Egypt", "coords": [30.0444, 31.2357]},
    {"name": "Johannesburg", "country": "South Africa", "coords": [-26.2041, 28.0473]},
    {"name": "Dakar", "country": "Senegal", "coords": [14.7167, -17.4677]},
    {"name": "Jerusalem", "country": "Israel", "coords": [31.7683, 35.2137]},
    {"name": "Riyadh", "country": "Saudi Arabia", "coords": [24.7136, 46.6753]},
    {"name": "New Delhi", "country": "India", "coords": [28.6139, 77.2090]},
    {"name": "Bangkok", "country": "Thailand", "coords": [13.7563, 100.5018]},
    {"name": "Ho Chi Minh City", "country": "Vietnam", "coords": [10.7769, 106.7009]},
    {"name": "Tokyo", "country": "Japan", "coords": [35.6895, 139.6917]},
    {"name": "Seoul", "country": "South Korea", "coords": [37.5665, 126.9780]},
    {"name": "Beijing", "country": "China", "coords": [39.9042, 116.4074]},
    {"name": "Shanghai", "country": "China", "coords": [31.2304, 121.4737]},
    {"name": "Hong Kong", "country": "China", "coords": [22.3193, 114.1694]},
    {"name": "Sydney", "country": "Australia", "coords": [-33.8688, 151.2093]},
    {"name": "Mexico City", "country": "Mexico", "coords": [19.4326, -99.1332]},
    {"name": "São Paulo", "country": "Brazil", "coords": [-23.5505, -46.6333]},
    {"name": "Kyiv", "country": "Ukraine", "coords": [50.4501, 30.5234]},
    {"name": "Warsaw", "country": "Poland", "coords": [52.2297, 21.0122]},
    {"name": "Baghdad", "country": "Iraq", "coords": [33.3152, 44.3661]}
]

for bureau in international_bureaus:
    folium.Marker(
        location=bureau["coords"],
        popup=folium.Popup(f"<b>{bureau['name']}, {bureau['country']}</b><br>New York Times Bureau", max_width=300),
        icon=intl_icon,
        tooltip=f"{bureau['name']}, {bureau['country']}"
    ).add_to(international_cluster)

# US bureaus with improved data structure
us_bureaus = [
    {"name": "Washington, D.C.", "state": "", "coords": [38.9072, -77.0369]},
    {"name": "Chicago", "state": "IL", "coords": [41.8781, -87.6298]},
    {"name": "Los Angeles", "state": "CA", "coords": [34.0522, -118.2437]},
    {"name": "San Francisco", "state": "CA", "coords": [37.7749, -122.4194]},
    {"name": "Seattle", "state": "WA", "coords": [47.6062, -122.3321]},
    {"name": "Miami", "state": "FL", "coords": [25.7617, -80.1918]},
    {"name": "Atlanta", "state": "GA", "coords": [33.7490, -84.3880]},
    {"name": "Houston", "state": "TX", "coords": [29.7604, -95.3698]},
    {"name": "Nashville", "state": "TN", "coords": [36.1627, -86.7816]},
    {"name": "Albany", "state": "NY", "coords": [42.6526, -73.7562]}
]

for bureau in us_bureaus:
    state_info = f", {bureau['state']}" if bureau['state'] else ""
    folium.Marker(
        location=bureau["coords"],
        popup=folium.Popup(f"<b>{bureau['name']}{state_info}</b><br>New York Times Bureau", max_width=300),
        icon=us_icon,
        tooltip=f"{bureau['name']}{state_info}"
    ).add_to(us_cluster)

# Add clusters to map
hq_cluster.add_to(m)
international_cluster.add_to(m)
us_cluster.add_to(m)

# Add layer control
folium.LayerControl(
    position="topright",
    collapsed=False
).add_to(m)

# Add professional, cleaner legend
legend_html = '''
<div style="position: fixed; 
     bottom: 20px; right: 20px; width: 250px;
     background-color: white; border:1px solid #ccc; z-index:9999; font-size:12px;
     border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);
     padding: 12px; font-family: Arial, sans-serif;">
     <div style="text-align: center; margin-bottom: 10px;"><b>THE NEW YORK TIMES</b></div>
     <div style="text-align: center; margin-bottom: 10px;"><b>Global Bureau Network</b></div>
     <hr style="margin: 5px 0; border-color: #eee;">
     <div style="display: flex; align-items: center; margin: 8px 0;">
        <i class="fa fa-building fa-lg" style="color:darkred; margin-right: 10px;"></i> 
        <span>Global Headquarters (1)</span>
     </div>
     <div style="display: flex; align-items: center; margin: 8px 0;">
        <i class="fa fa-newspaper fa-lg" style="color:darkblue; margin-right: 10px;"></i> 
        <span>International Bureaus (26)</span>
     </div>
     <div style="display: flex; align-items: center; margin: 8px 0;">
        <i class="fa fa-newspaper fa-lg" style="color:darkgreen; margin-right: 10px;"></i> 
        <span>US Bureaus (10)</span>
     </div>
     <hr style="margin: 5px 0; border-color: #eee;">
     <div style="font-size: 10px; color: #666; text-align: center;">
        © The New York Times Company, 2025
     </div>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Add a title to the map
title_html = '''
<div style="position: fixed; 
     top: 20px; left: 50%; transform: translateX(-50%);
     width: 400px; background-color: rgba(255, 255, 255, 0.8);
     border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);
     text-align: center; padding: 10px; z-index: 9998; font-family: Arial, sans-serif;">
     <h3 style="margin: 0; color: #333;">THE NEW YORK TIMES GLOBAL PRESENCE</h3>
</div>
'''
m.get_root().html.add_child(folium.Element(title_html))

# Add additional CSS for professional styling
css = '''
<style>
.leaflet-popup-content-wrapper {
    border-radius: 4px;
    box-shadow: 0 3px 14px rgba(0,0,0,0.2);
}
.leaflet-popup-content {
    margin: 13px 19px;
    line-height: 1.4;
    font-family: Arial, sans-serif;
}
.leaflet-popup-content b {
    color: #1a1a1a;
}
.leaflet-popup-tip-container {
    margin-top: -1px;
}
</style>
'''
m.get_root().html.add_child(folium.Element(css))

# Save the map to an HTML file
m.save('nyt_global_offices_map.html')

print("Map created successfully with enhanced professional styling!")