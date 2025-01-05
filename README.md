# Drawaria CanvasPic

Drawaria CanvasPic is a Python script that automates the process of drawing an image on the Drawaria online canvas using Selenium and JavaScript. The script downloads an image, processes its pixel data, and then uses Selenium to interact with the Drawaria website, injecting JavaScript to draw the image pixel by pixel on the canvas.

## Features

- **Image Downloading**: Downloads an image from a specified URL.
- **Pixel Processing**: Converts the image into RGBA format and extracts pixel data.
- **Canvas Drawing**: Uses Selenium to automate the drawing process on the Drawaria canvas.
- **WebSocket Integration**: Includes basic WebSocket functionality for sending and receiving canvas data (currently under development).

## Requirements

- Python 3.x
- Selenium
- Pillow (PIL)
- ChromeDriver

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Drawaria-CanvasPic.git
   cd Drawaria-CanvasPic
   ```

2. **Install the required Python packages**:
   ```bash
   pip install selenium pillow requests
   ```

3. **Download ChromeDriver**:
   - Download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Place the `chromedriver.exe` in a directory and update the `chrome_driver_path` variable in the script with the correct path.

## Usage

1. **Update the image URL**:
   - Replace the `image_url` variable in the script with the URL of the image you want to draw.

2. **Update the Drawaria room URL**:
   - Replace the `url` variable with the URL of the Drawaria room where you want to draw the image.

3. **Run the script**:
   ```bash
   python drawaria_canvaspic.py
   ```

## How It Works

1. **Image Processing**:
   - The script downloads the image from the specified URL.
   - It converts the image to RGBA format and extracts the pixel data.
   - The pixel data is then formatted into a JavaScript array.

2. **Canvas Drawing**:
   - Selenium is used to open the Drawaria website in a Chrome browser.
   - The script injects JavaScript code into the page to draw the image pixel by pixel on the canvas.

3. **WebSocket Integration**:
   - The script includes basic WebSocket functionality for sending and receiving canvas data. This part is currently under development and may require further refinement.

## Notes

- **Browser Automation**: The script uses Selenium to automate the browser. Ensure that you have the correct version of ChromeDriver installed and that it matches your Chrome browser version.
- **WebSocket**: The WebSocket functionality is experimental and may not work as expected. It is intended for future enhancements to allow real-time collaboration or data sharing.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for browser automation.
- [Pillow (PIL)](https://pillow.readthedocs.io/) for image processing.
- [Drawaria](https://drawaria.online/) for providing the canvas platform.

---

Feel free to customize this description further to better fit your repository and project goals!