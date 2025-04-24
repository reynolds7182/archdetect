## ARCH-DETECT

## Link to project video recording:  [Video Walk-Through](https://artslondon-my.sharepoint.com/:v:/g/personal/c_reynolds1220231_arts_ac_uk/EZURuEAE6xBLhM1utW2QI1QB25tHZktt9mRi2NcAyT7FVg?e=OVPiLd)

## Overview
ARCH-DETECT is an interactive web application that identifies architectural styles from images. Created for tourists and architecture enthusiasts exploring London's rich architectural landscape, it provides immediate insights about buildings. Simply snap a photo or upload an image to discover its architectural style, historical context, and similar notable structures.

## Background
The project initially explored building a neural network trained on architectural datasets but pivoted to using a vision-language model (VLM) for more comprehensive analysis. After research and consultation, Ollama with the LLaVA model was selected as the ideal solution, as it combines "machine vision and semantic processing techniques to make sense of the relationship in and between objects in images." [2]

## Features
- Dual Input Methods: Take a photo in real-time or upload an existing image
- Comprehensive Analysis: Identifies architectural styles, time periods, and key characteristics
- Educational Content: Provides information about notable architects and similar buildings
- User-Friendly Interface: Simple, intuitive design built with Streamlit

## Requirements
- Python 3.7+
- Streamlit
- Ollama (with LLaVA model installed)
- PIL (Python Imaging Library)
- Internet connection (for model inference)

# Setup instructions:

1. Clone this repository or download the source code
```
git clone https://git.arts.ac.uk/24001912/AI-4-Media-Project-Claire-Reynolds.git
cd project.py
```
2. Install the Streamlit and Ollama packages by using the line below 
```
pip install streamlit ollama
```

3. Ensure you have Ollama installed and the LLaVA model pulled
```
ollama pull llava
```

4. Run Arch-Detect in your browser by typing this line in your terminal/command line. 
```
streamlit run project.py
```
5. Upload / snap a photo and follow the instructions on the page!


## How It Works
ARCH-DETECT uses the multimodal LLaVA model through Ollama to analyze images.

The application:
1. Converts the uploaded or captured image into base64 encoding
2. Sends the encoded image to the LLaVA model with specific prompts
3. Analyzes the response to identify:
    a. Whether the image contains any notable buildings
    b. The architectural style and time period
    c. Key characteristics defining the style
    d. Notable architects associated with the style
    e. Similar famous buildings around the world



## Limitations

- May occasionally misidentify buildings with similar architectural features
- Performance varies with image quality and clarity
- Can provide different classifications for the same building in different submissions
- Works best with distinct architectural styles and well-known landmarks

## LLM Disclaimer
Used Claude to format, check grammary, and make my README file more concise. 

## Citations: 
[1] Anthropic (2025) Claude [AI assistant]. Available at: https://claude.ai (Accessed: 21 March 2025).
[2]Ollama (2025) LLaVA: Multimodal vision-language model. Available at: https://ollama.ai (Accessed: 19 March 2025).


