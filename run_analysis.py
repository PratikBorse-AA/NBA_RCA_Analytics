#!/usr/bin/env python3

"""Entry point for NBA RCA Analytics run script (placeholder)."""
from src.data_loader import DataLoader
from src.validator import DataValidator

def main():

    loader = DataLoader()
    df = loader.load_data()

    validator = DataValidator()
    validator.validate(df)

    print("\nDataset Loaded Successfully!")
if __name__ == "__main__":
    main()
