import fetch from 'node-fetch';

const owner = 'LineIndent';
const repoName = 'reflexify';

// GitHub REST API URL to get the repository information
const apiUrl = `https://api.github.com/repos/${owner}/${repoName}`;

// Function to format a number in shorthand like 'k'
function formatNumberShorthand(number) {
    if (number >= 1000) {
        return (number / 1000).toFixed(1) + 'k';
    }
    return number.toString();
}


// Function to fetch and display repository information, including the latest release
async function getRepoInfo() {
    try {
        // Dynamically import the 'node-fetch' module as an ES module
        // const fetch = (await import('../node-fetch')).default;


        // Send an HTTP GET request to the GitHub API
        const response = await fetch(apiUrl);
        const repoInfo = await response.json();
        
        const name = document.getElementById("name")
        console.log(name)
        

        // NOTE * KEEP BELOW CODE * 
        // const response_html = await fetch(apiUrl);
        // const html = await response_html.text();

        // // Create a DOM using jsdom
        // const { window } = new (await import('jsdom')).JSDOM(html);
        // const document = window.document;
        

        // Check if the response contains the desired information
        if (response.status === 200) {
            const starsCount = repoInfo.stargazers_count;
            const forksCount = repoInfo.forks_count;
            
            // NOTE * KEEP THE BELOW CODE *
            // // Extract the latest release version
            // const releaseElement = document.querySelector('.css-truncate.css-truncate-target.text-bold.mr-2');
            // const latestRelease = releaseElement ? releaseElement.textContent.trim() : 'N/A';


            // Fetch the latest release information
            const releaseUrl = `${apiUrl}/releases/latest`;
            const releaseResponse = await fetch(releaseUrl);
            const releaseInfo = await releaseResponse.json();
            const latestRelease = releaseInfo.tag_name;

            console.log(`Stars: ${formatNumberShorthand(starsCount)}`);
            console.log(`Forks: ${formatNumberShorthand(forksCount)}`);
            console.log(`Latest Release: ${latestRelease}`);
        } else {
            console.log('Error fetching repository information.');
        }
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Call the function to get and display repository information
getRepoInfo();
