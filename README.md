# Pix2Pix Implementation

## Overview
This repository is part of the IIT Madras AI Club Deputy Coordinator Mini Project that aims at reimplementing the **Pix2Pix** paper. The project follows a structured week-wise approach, covering both **theoretical concepts** and **practical implementations** of **Generative Adversarial Networks (GANs)** and **Conditional GANs (cGANs)**.

## Objectives
- Develop a step-by-step understanding of the Pix2Pix model.
- Explore the theoretical foundations of GANs and cGANs.
- Gain hands-on experience with machine learning libraries such as TensorFlow and PyTorch.

## About Pix2Pix
The **Pix2Pix** model, introduced in *"Image-to-Image Translation with Conditional Adversarial Networks"* by Isola et al., is a supervised deep learning method designed for various image-to-image translation tasks. It employs a **U-Net-based generator** and a **PatchGAN discriminator**, trained with adversarial and L1 losses.

## Getting Started
To follow along with the course structure, navigate through the respective week folders and explore both the theoretical notes and code implementations.

## References
- [Pix2Pix Paper](https://arxiv.org/abs/1611.07004)
- [Original Implementation](https://github.com/phillipi/pix2pix)


## Data Files Structure

### Large Files Handling

To comply with GitHub's file size limitations (50MB maximum recommended size), the large data files used in this project have been split into smaller chunks:

- **train_data_sketch.txt** (~80MB) → split into multiple `train_data_sketch_part_*` files
- **train_data_full.txt** (~80MB) → split into multiple `train_data_full_part_*` files

All chunks are stored in the `data_chunks` directory.

### Recombining Data Files

To recombine the chunks into their original files for use in the project, use the included `combine_data_files.sh` script:

```bash
# Make the script executable (if needed)
chmod +x combine_data_files.sh

# Run the script
./combine_data_files.sh
```

This will regenerate the original files:
- `train_data_sketch.txt`
- `train_data_full.txt`

### Manual Recombination

If the script doesn't work for you, you can manually recombine the files using these commands:

```bash
# For train_data_sketch.txt
cat data_chunks/train_data_sketch_part_* > train_data_sketch.txt

# For train_data_full.txt
cat data_chunks/train_data_full_part_* > train_data_full.txt
```
