// GitHub repository owner and name
const owner = '<owner>';
const repoName = '<repo>';

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
        const fetch = (await import('node-fetch')).default;

        // Send an HTTP GET request to the GitHub API
        const response = await fetch(apiUrl);
        const repoInfo = await response.json();
        
        // Check if the response contains the desired information
        if (response.status === 200) {
            const starsCount = repoInfo.stargazers_count;
            const forksCount = repoInfo.forks_count;
            
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

