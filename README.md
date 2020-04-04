# Which dog are you?

[![HitCount](http://hits.dwyl.io/AlbertSuarez/which-dog-are-you.svg)](http://hits.dwyl.io/AlbertSuarez/which-dog-are-you)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/which-dog-are-you.svg)](https://GitHub.com/AlbertSuarez/which-dog-are-you/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/which-dog-are-you.svg)](https://GitHub.com/AlbertSuarez/which-dog-are-you/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AlbertSuarez/which-dog-are-you.svg)](https://github.com/AlbertSuarez/which-dog-are-you)

🐶 Dog and face person matcher based on image similarity

## Results

### Input

<p align="center">
  <img alt="EasyCam" src="docs/images/example_input_image.jpg" width="30%"/>
</p>

### Output

<p align="center">
  <img alt="EasyCam" src="docs/images/example_output_image.jpg" width="30%"/>
</p>

## Summary

### Inspiration

This project came to my mind in order to improve the experience seen in all the Instagram filters where everything is random. With that being said, I wanted to really know which dog is the one that is most similar to me. Yeah, it's random. I know.

### What it does

From an image (image path or image URL), it returns the most similar dog given the [Standford Dogs dataset](https://www.kaggle.com/jessicali9530/stanford-dogs-dataset/data#). Simple and beautiful.

### How I built it

Using Python 3.7, Tensorflow, NMSLIB, NumPy and Pillow, it builds a similarity index where I extract the features of the input image versus the built index and get the closest one.

### Challenges I ran into

To be honest, I wanted to do another project (completely different from this one) in this hackathon (HackFromHome Round 2) but I got stuck after several hours and realized that was impossible. Yeah, what a pity.

That's why I decided to move to this project.

### Accomplishments that I'm proud of

Building this random thing in less than 3 hours.

### What's next for Which dog are you?

A lot of things, like a beautiful UI and getting this deployed somewhere.

## Project

### Requirements

1. Python 3.7+.

### Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

### Usage

To run the pipeline, please execute the following from the root directory:

1. Setup virtual environment

2. Install dependencies

    ```bash
    pip3 install -r requirements.lock
    ```

3. Download the [Standford Dogs dataset](https://www.kaggle.com/jessicali9530/stanford-dogs-dataset/data#) into `data/standford-dogs-dataset.zip`

4. Prepare dataset

    ```bash
    python3 -m src.prepare_dataset [--images_per_race N]
    ```

5. Build similarity index

    ```bash
    python3 -m src.build
    ```

6. Run similarity search

    ```bash
    python3 -m src.run [--image_url https://example.org/image.jpg] [--image_path image.jpg] [--show]
    ```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © Which dog are you?
