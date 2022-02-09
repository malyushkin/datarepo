"""GitHub Markdown README generator"""

from datetime import datetime
import sys
import yaml

FILE = dict(yml_name="repo.yaml",
            md_name="README.md")

KEY = dict(title_key="title",
           code_key="code",
           articles_key="articles",
           books_key="books",
           expert_interviews_key="expert_interviews",
           job_interviews_key="job_interviews",
           reports_key="reports"
           )


def write_md_section_title(section_title):
    """Write course section title in Markdown"""
    md.write(f"## {section_title}")
    md.write("\n\n")


def write_md_section_list(section_list):
    """Write course section list in Markdown"""
    md.write("\n\n")
    md.write("|Year|Title|Authors|Extra|Tags|Status|")
    # md.write(section_list.keys())
    md.write("\n")
    md.write("|----|-----|-------|-----|----|------|")
    md.write("\n")


    for section_list_item in section_list:

        # Year
        if 'year' in section_list_item:
            md.write("|" + str(section_list_item['year']))
        else:
            md.write("| ")

        # Title
        md.write(f"|")
        if 'language' in section_list_item:
            md.write(f" _({section_list_item['language']})_ ")

        if 'url' in section_list_item:
            md.write("[" + section_list_item['title'] + "]") # + url
            md.write("(" + section_list_item['url'] + ")")
        else:
            md.write(section_list_item['title'])

        # Authors
        if 'authors' in section_list_item:
            md.write("|" + ", ".join(section_list_item['authors']))
        else:
            md.write("| ")

        # Extra
        if 'extra' in section_list_item:
            md.write("|" + ", ".join(map(lambda extra_item: f"[{extra_item.split('_')[1].title()}]({section_list_item['extra'].get(extra_item)})", section_list_item['extra'].keys())))
        else:
            md.write("| ")

        # Tags
        if 'tags' in section_list_item:
            md.write("|" + ", ".join(map(lambda tag: f"`{tag}`", section_list_item['tags'])))
        else:
            md.write("| ")

        md.write("|")
        md.write("\n")

    md.write("\n")


with open(FILE['yml_name'], "r", encoding="utf-8") as yml:
    course = yaml.safe_load(yml)

with open(FILE['md_name'], "w", encoding="utf-8") as md:
    md.write(f"# {course[KEY['title_key']]}")
    md.write("\n\n")

    if "sections" not in course:
        sys.exit()

    # Sections
    for section in course['sections']:
        write_md_section_title(section[KEY['title_key']])

        # Webinars
        if KEY['reports_key'] in section:
            md.write("### Reports")
            write_md_section_list(section[KEY['reports_key']])

        # Books
        if KEY['books_key'] in section:
            md.write("### Books")
            write_md_section_list(section[KEY['books_key']])

        # Articles
        if KEY['articles_key'] in section:
            md.write("### Articles")
            write_md_section_list(section[KEY['articles_key']])

        # Job Interviews
        if KEY['job_interviews_key'] in section:
            md.write("### Job Interviews")
            md.write("\n\n")
            write_md_section_list(section[KEY['job_interviews_key']])

        # Expert Interviews
        if KEY['expert_interviews_key'] in section:
            md.write("### Expert Interviews")
            md.write("\n\n")
            write_md_section_list(section[KEY['expert_interviews_key']])
