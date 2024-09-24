import asyncio
from playwright.async_api import async_playwright

async def download_file(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        htmlText = """
    <html>
        <body>
            <a href='""" + url + """'>Download file</a>
        </body>
    </html>
"""

        await page.set_content(htmlText)

        # Click the download link
        async with page.expect_download() as download_info:
            await page.click('a', modifiers=["Alt"]) 
        download = await download_info.value

        # Save the downloaded file
        await download.save_as('downloaded_file.ext')  # Replace with the desired file name and extension

        await browser.close()


downloadUrl = "https://www.rd.usda.gov/media/file/download/ffb-daily-rates.pdf"

asyncio.run(download_file(url=downloadUrl))