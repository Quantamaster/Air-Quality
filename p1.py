import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import folium
import imageio.v2 as imageio
import os
from datetime import datetime, timedelta


# --- Step 1 & 2: Data Acquisition (Illustrative - CPCB API details would be complex) ---
def fetch_cpcb_data_for_day(date_str):
    stations_data = {
        'Anand Vihar': {'lat': 28.6479, 'lon': 77.3194, 'aqi_data': {}},
        'Dwarka-Sector 8': {'lat': 28.5836, 'lon': 77.0601, 'aqi_data': {}},
        'ITO': {'lat': 28.6186, 'lon': 77.2307, 'aqi_data': {}},
        'Rohini': {'lat': 28.7325, 'lon': 77.1197, 'aqi_data': {}},
        'Delhi Cantt': {'lat': 28.6102, 'lon': 77.1278, 'aqi_data': {}},
    }
    current_date = datetime.strptime(date_str, '%Y-%m-%d')
    for hour in range(24):
        time_key = current_date + timedelta(hours=hour)
        for station_name in stations_data:
            aqi = 50 + (hour * 5) + (hash(station_name + str(hour)) % 100)  # Dummy AQI
            stations_data[station_name]['aqi_data'][time_key] = aqi

    flat_data = []
    for station_name, details in stations_data.items():
        for time_stamp, aqi_val in details['aqi_data'].items():
            flat_data.append({
                'Station': station_name,
                'Latitude': details['lat'],
                'Longitude': details['lon'],
                'Timestamp': time_stamp,
                'AQI': aqi_val
            })
    return pd.DataFrame(flat_data)


# --- Step 3: Data Collection and Preprocessing (Conceptual) ---
start_date = datetime(2024, 6, 1)  # Example month
end_date = datetime(2024, 6, 30)
all_data_frames = []

current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    print(f"Fetching data for {date_str}...")
    daily_df = fetch_cpcb_data_for_day(date_str)
    all_data_frames.append(daily_df)
    current_date += timedelta(days=1)

df_aqi = pd.concat(all_data_frames, ignore_index=True)
df_aqi['Timestamp'] = pd.to_datetime(df_aqi['Timestamp'])
df_aqi.sort_values(by=['Timestamp', 'Station'], inplace=True)

# --- Step 4 & 5: Visualization and GIF Generation ---
output_folder = 'aqi_frames'
os.makedirs(output_folder, exist_ok=True)

# Define AQI categories and colors
aqi_bins = [0, 50, 100, 200, 300, 400, 500]  # These are the bin *edges*
aqi_labels = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor',
              'Severe']  # These are the *labels for the ranges*
aqi_colors = ['#00E676', '#FFFF00', '#FFC107', '#FF9800', '#F44336',
              '#880E4F']  # Green, Yellow, Orange, Red, Dark Red, Maroon

cmap = mcolors.ListedColormap(aqi_colors)
norm = mcolors.BoundaryNorm(aqi_bins, cmap.N)

# Calculate tick locations for labels - these should be the midpoints of the bins
aqi_tick_locations = [(aqi_bins[i] + aqi_bins[i + 1]) / 2 for i in range(len(aqi_bins) - 1)]

images = []
# Process a subset of unique timestamps for demonstration to avoid excessively long runtimes
# For a full month, consider sampling every N hours or using daily averages.
# Here, I'll process a small subset for demonstration. In your actual code, use `unique_timestamps`.
# Example: Process only specific timestamps (e.g., noon each day)
unique_timestamps_to_process = sorted([ts for ts in df_aqi['Timestamp'].unique() if pd.to_datetime(ts).hour == 12])
if not unique_timestamps_to_process:  # Fallback if 12 PM data not available for any day
    unique_timestamps_to_process = sorted(df_aqi['Timestamp'].unique())[::24]  # Take one frame per day (roughly)

for i, timestamp_val in enumerate(unique_timestamps_to_process):  # Use filtered timestamps
    current_time_df = df_aqi[df_aqi['Timestamp'] == timestamp_val].copy()

    if current_time_df.empty:
        continue

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(current_time_df['Longitude'], current_time_df['Latitude'],
               c=current_time_df['AQI'], cmap=cmap, norm=norm, s=200, edgecolors='black', alpha=0.8)

    for idx, row in current_time_df.iterrows():
        ax.text(row['Longitude'] + 0.01, row['Latitude'] + 0.01, row['Station'], fontsize=8)

    ax.set_xlim(76.8, 77.6)  # Approx longitude for Delhi
    ax.set_ylim(28.4, 28.9)  # Approx latitude for Delhi

    ax.set_title(f"Delhi AQI: {pd.to_datetime(timestamp_val).strftime('%Y-%m-%d %H:%M')}")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    # Use the calculated aqi_tick_locations for the colorbar ticks
    cbar = fig.colorbar(sm, ax=ax, orientation='vertical', ticks=aqi_tick_locations, pad=0.05)
    cbar.set_ticklabels(aqi_labels)  # Now the number of ticks (6) matches the number of labels (6)
    cbar.set_label("Air Quality Index (AQI)")

    frame_filename = os.path.join(output_folder, f"aqi_frame_{i:04d}.png")
    plt.savefig(frame_filename)
    plt.show()
    plt.close(fig)
    images.append(imageio.imread(frame_filename))

# Create GIF
imageio.mimsave('delhi_aqi_animation.gif', images, fps=5)

print("GIF generated: delhi_aqi_animation.gif")