# Netflix Movies Analysis Streamlit App

This is a Streamlit application for analyzing Netflix movie data. The app provides various features to explore and visualize movies based on different attributes such as duration, genre, country, and type.

## Features

1. **Movies Less than 60 Minutes**: View a list of movies with a duration of less than 60 minutes.
2. **Movie Duration Scatter Plot**: Visualize movie durations by year of release with different colors representing genres.
3. **Genre Analysis**: Filter and view movies based on selected genres along with their descriptions.
4. **Country Analysis**: Filter and view movies based on the selected country along with their descriptions.
5. **Type of Movies**: Filter and view movies based on their type (e.g., movie, series) along with their descriptions.

## Setup

### Prerequisites

- Python 3.6 or higher
- Streamlit
- Pandas
- Matplotlib

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/NoorFatimaAfzal/Bytewise-fellowship.git
    ```

2. Navigate into the project directory:

    ```sh
    cd Bytewise-fellowship
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```plaintext
    streamlit
    pandas
    matplotlib
    ```

## Usage

1. Place your `netflix_data.csv` file in the project directory.
2. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

3. Access the app in your web browser at `http://localhost:8501`.

## How to Use the App

1. **Movies Less than 60 Minutes**:
    - Select this option to view movies with a duration of less than 60 minutes.

2. **Movie Duration Scatter Plot**:
    - Choose this option to see a scatter plot of movie durations by release year, with different colors representing genres.

3. **Genre Analysis**:
    - Select a genre from the dropdown to filter movies by genre. You can also view all genres.

4. **Country Analysis**:
    - Select a country from the dropdown to filter movies by country. You can also view movies from all countries.

5. **Type of Movies**:
    - Choose a type of movie from the dropdown to filter by type (e.g., movie, series). You can also view all types.

## Contributing

Feel free to fork the repository and submit pull requests. Please ensure that your contributions are well-documented and tested.

## Contact

For any questions or issues, please contact noorfatimaafzalbutt@gmail.com.

