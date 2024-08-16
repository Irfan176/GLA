## Data

The project uses two main data structures:

1. `reasons_data`: A dictionary containing reasons for using educational resources, each with a complexity and interactiveness rating.
2. `individuals`: A list of dictionaries, each representing an individual with a name and a list of reasons.

## Classification

Individuals are classified based on their average complexity and interactiveness scores:

- Logical: Low complexity (< 3.5), Low interactiveness (< 3)
- Visual: Low complexity (< 3.5), High interactiveness (>= 3)
- Traditional: High complexity (>= 3.5), Low interactiveness (< 3)
- Active: High complexity (>= 3.5), High interactiveness (>= 3)

## Output

The script produces two outputs:

1. A scatter plot visualizing the classification of individuals.
2. Console output showing the classification of each individual.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.