# Data Visualization

## Assignment 4: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?
        I used Python, specifically leveraging libraries such as Matplotlib and Seaborn, for creating the data visualization.
        
    > Who is your intended audience? 
        The intended audience includes policy analysts, social workers, and the general public who are interested in understanding the impact of private income on GAINS payment eligibility.
    > What information or message are you trying to convey with your visualization? 
       The visualization aims to convey the relationship between private income levels and GAINS payment eligibility, showing how varying levels of private income affect the amount of GAINS payments for single seniors and senior couples.
    > What design principles (substantive, perceptual, aesthetic) did you consider when making your visualization? How did you apply these principles? With what elements of your plots? 
        Substantive: Focused on clarity and relevance by choosing to display the income thresholds and corresponding GAINS payments.
        Perceptual: Used a clear color scheme to differentiate between income levels and payment amounts, with labeled axes and annotations for key data points.
        Aesthetic: Ensured simplicity and balance by minimizing clutter and using a consistent style for fonts and labels.
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
        Python code is fully reproducible; anyone with access to the dataset and code can generate the same visualization. This ensures consistency and accuracy in the results.
    > How did you ensure that your data visualization is accessible?  
        I used high-contrast colors and descriptive labels to make the visualization readable for individuals with visual impairments. I also ensured the plot is compatible with screen readers by providing alternative text descriptions.
    > Who are the individuals and communities who might be impacted by your visualization?  
        Seniors, policymakers, and financial advisors are directly impacted, as the visualization provides insights into GAINS payment eligibility that could inform financial planning and policy decisions.
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
        I included features directly related to the relationship between private income and GAINS payments, excluding extraneous data to keep the visualization focused and clear.
    > What ‘underwater labour’ contributed to your final data visualization product?
        This involved data cleaning, coding, testing different visualization approaches, and ensuring the visualization was accurate and clear.

    >> Excel Visualization
    > What software did you use to create your data visualization?
        I used Microsoft Excel to create the data visualization.

    > Who is your intended audience?
        The intended audience includes seniors, financial advisors, and policymakers who are interested in understanding the differences in GAINS payments between single seniors and senior couples.

    > What information or message are you trying to convey with your visualization?
        The visualization aims to compare the maximum GAINS payments for single seniors and senior couples, highlighting how payments differ based on household status.

    > What design principles (substantive, perceptual, aesthetic) did you consider when making your visualization? How did you apply these principles? With what elements of your plots?
        Substantive: Focused on clarity and relevance by clearly showing the differences in GAINS payments between the two groups.
        Perceptual: Used contrasting colors to differentiate between singles and couples, with a clear legend and data labels for easy interpretation.
        Aesthetic: Ensured simplicity by using a straightforward bar chart with minimalistic design elements to keep the focus on the data.
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
        Excel visualizations can be reproduced by sharing the Excel file, but there might be slight variations if the file is opened in different versions of Excel. This can impact the consistency of the visualization.

    > How did you ensure that your data visualization is accessible?
        I used high-contrast colors and added data labels directly on the chart. The visualization is designed to be straightforward, with clear text descriptions for better accessibility.

    > Who are the individuals and communities who might be impacted by your visualization?
        Seniors, financial advisors, and policymakers are the primary groups impacted by this visualization, as it provides clear insights into GAINS payments that can inform financial planning and policy-making.

    > How did you choose which features of your chosen dataset to include or exclude from your visualization?
        I focused on the maximum GAINS payments and the corresponding private income thresholds, excluding other unrelated data points to maintain clarity and focus.

    > What ‘underwater labour’ contributed to your final data visualization product?
        This included data entry, formatting the chart, adjusting design elements for clarity, and ensuring the final product was visually appealing and informative.


- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `HH:MM AM/PM - DD/MM/YYYY`
* The branch name for your repo should be: `assignment-4`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_4.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-4`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack at `#cohort-3-help`. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
