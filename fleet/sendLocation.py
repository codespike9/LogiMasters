import geocoder
import asyncio
import websockets
import json

async def fetch_and_send_location(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            # Fetch current location based on IP address
            print("a")
            location = get_current_location()
            if location:
                # Extract latitude and longitude
                address=location

                # Construct the message to send
                message = {"address":address }

                # Send the message to the WebSocket server
                await websocket.send(json.dumps(message))
                print(f"Sent location to WebSocket: {message}")

            # Adjust the sleep duration based on your requirements
            await asyncio.sleep(2)  # Fetch location every 10 seconds

def get_current_location():
    try:
        # Use geocoder to get location based on IP address
        g = geocoder.ip('me')
        print(g.latlng)
        if g.latlng:
            return g.latlng  # Return geocoder response object
        else:
            print("Location not found.")
            return None
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None

# Replace "ws://example.com/socket" with your WebSocket server URI
websocket_uri = "ws://127.0.0.1:8001/ws/fleettracking/first/"

# Create and set up a new event loop
async def main():
    while True:
        try:
            await fetch_and_send_location(websocket_uri)
        except Exception as e:
            print(f"An error occurred: {e}")
            # Retry after a delay
            await asyncio.sleep(10)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
