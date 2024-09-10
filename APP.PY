import streamlit as st
import pandas as pd

# Define platform data
data = {
    "Platform": ["StackSocial", "Dealify", "PitchGround", "SaasMantra", "GrabLTD", "BitsDuJour", 
                 "DealMirror", "Lifetime.tech", "The Software Shop", "LTD Hunt", "DigitalThink", 
                 "SaaSPirate", "StoreApps Deals", "Toolbox", "Product Hunt", "SharewareOnSale", 
                 "FounderDeals", "SoftwareFindr", "DealFuel", "Startup Stash", "BuySoftwareDeals", 
                 "FomoHunt", "AppZumo", "GearBest", "WeLoveLTD"],
    "Description": [
        "Deals on software, online courses, and gadgets.", 
        "Lifetime deals and discounts on SaaS tools for growth hackers and marketers.",
        "Early-stage SaaS lifetime deals with a focus on startups.",
        "Lifetime deals on SaaS products for entrepreneurs and businesses.",
        "Lifetime software deals tailored for marketers, entrepreneurs, and designers.",
        "Daily software deals with significant discounts, sometimes up to 100%.",
        "Discounted software deals for small businesses and marketers.",
        "SaaS lifetime deals and software discounts, focusing on business tools.",
        "Offers discounts and lifetime deals on software for various niches.",
        "Aggregator of lifetime deals on SaaS tools and platforms.",
        "Lifetime software deals focused on business tools and growth solutions.",
        "Curated deals on SaaS tools for growth hackers and startups.",
        "Lifetime deals and discounted software for WooCommerce and WordPress.",
        "Lifetime deals and discounts for SaaS products geared towards entrepreneurs.",
        "Features new and innovative software and tech products, often with exclusive deals.",
        "Offers free and discounted software on both short-term and lifetime licenses.",
        "Software deals tailored specifically for startup founders and entrepreneurs.",
        "Features a mix of deals and comparisons for SaaS tools, with occasional lifetime offers.",
        "Daily deals on web design and development tools, templates, and software.",
        "A curated directory of tools and resources for startups, with occasional deal listings.",
        "Discounted software deals for various categories, including lifetime options.",
        "Marketplace for discounted SaaS products and tools for growth hackers.",
        "Aggregates and showcases lifetime deals for entrepreneurs and startups.",
        "Primarily focused on gadgets, they sometimes offer deals on software and tech tools.",
        "Community-driven platform showcasing lifetime deals on SaaS and business tools."
    ],
    "Website URL": [
        "https://stacksocial.com", "https://dealify.com", "https://pitchground.com", 
        "https://saasmantra.com", "https://grabltd.com", "https://bitsdujour.com", 
        "https://dealmirror.com", "https://lifetime.tech", "https://thesoftware.shop", 
        "https://ltdhunt.com", "https://digitalthink.io", "https://saaspirate.com", 
        "https://storeapps.org", "https://toolboxdeals.com", "https://producthunt.com", 
        "https://sharewareonsale.com", "https://founderdeals.com", "https://softwarefindr.com", 
        "https://dealfuel.com", "https://startupstash.com", "https://buysoftwaredeals.com", 
        "https://fomohunt.com", "https://appzumo.com", "https://gearbest.com", "https://weloveltd.com"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit App
st.title("SaaS Lifetime Deals & Software Platforms Management")

# Show the DataFrame in a table
st.subheader("List of Platforms and Details")
st.dataframe(df)

# Sidebar filters
st.sidebar.title("Filter Options")
selected_platform = st.sidebar.multiselect("Select Platform(s)", df['Platform'].unique())
selected_keyword = st.sidebar.text_input("Search by Keyword (Description)")

# Apply filters
filtered_df = df.copy()

if selected_platform:
    filtered_df = filtered_df[filtered_df['Platform'].isin(selected_platform)]

if selected_keyword:
    filtered_df = filtered_df[filtered_df['Description'].str.contains(selected_keyword, case=False, na=False)]

# Show filtered results
st.subheader("Filtered Results")
st.dataframe(filtered_df)

# Add new entries form
st.subheader("Add a New Platform")
new_platform = st.text_input("Platform Name")
new_description = st.text_area("Description")
new_website = st.text_input("Website URL")

if st.button("Add Platform"):
    if new_platform and new_description and new_website:
        # Add the new platform to the DataFrame
        new_row = {"Platform": new_platform, "Description": new_description, "Website URL": new_website}
        df = df.append(new_row, ignore_index=True)
        st.success(f"Added {new_platform} successfully!")
    else:
        st.error("Please fill out all fields to add a platform.")

# Show updated DataFrame
st.subheader("Updated Platform List")
st.dataframe(df)
