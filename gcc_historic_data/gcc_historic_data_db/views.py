from django.core.paginator import Paginator
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

import csv

def query_q1(request):
    custom_query = """SELECT
    department,
    job,
    COUNT(id) FILTER (WHERE q = 1) AS q1,
    COUNT(id) FILTER (WHERE q = 2) AS q2,
    COUNT(id) FILTER (WHERE q = 3) AS q3,
    COUNT(id) FILTER (WHERE q = 4) AS q4
    FROM
        (
        SELECT 
            e.id,
            d.department,
            j.job,
            EXTRACT(quarter from e.datetime) AS q
        FROM
            employees_data.hired_employees e
            INNER JOIN employees_data.departments d
                ON d.id = e.department_id
            INNER JOIN employees_data.jobs j
                ON j.id = e.job_id
        WHERE 
            EXTRACT(year FROM datetime) = 2021
        ) as quarters
    GROUP BY
        department,
        job
    ORDER BY
        department,
        job
    """

    data = []
    # Execute the custom query and fetch the data
    with connection.cursor() as cursor:
        cursor.execute(custom_query)
        column_names = [desc[0] for desc in cursor.description]
        for row in cursor:
            data.append(dict(zip(column_names, row)))

    # Paginate the results
    page_number = request.GET.get(
        "page", 1
    )  # Get the current page number from the request
    items_per_page = 20  # Number of items to display per page
    paginator = Paginator(data, items_per_page)
    page = paginator.get_page(page_number)


    return render(request, "q1.html", {"page": page, "columns": column_names})

def get_q1(request):
    custom_query = """SELECT
    department,
    job,
    COUNT(id) FILTER (WHERE q = 1) AS q1,
    COUNT(id) FILTER (WHERE q = 2) AS q2,
    COUNT(id) FILTER (WHERE q = 3) AS q3,
    COUNT(id) FILTER (WHERE q = 4) AS q4
    FROM
        (
        SELECT 
            e.id,
            d.department,
            j.job,
            EXTRACT(quarter from e.datetime) AS q
        FROM
            employees_data.hired_employees e
            INNER JOIN employees_data.departments d
                ON d.id = e.department_id
            INNER JOIN employees_data.jobs j
                ON j.id = e.job_id
        WHERE 
            EXTRACT(year FROM datetime) = 2021
        ) as quarters
    GROUP BY
        department,
        job
    ORDER BY
        department,
        job
    """

    data = []
    # Execute the custom query and fetch the data
    with connection.cursor() as cursor:
        cursor.execute(custom_query)
        column_names = [desc[0] for desc in cursor.description]
        for row in cursor:
            data.append(row)

    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=q1_data.csv'
    writer = csv.writer(response)
    writer.writerow(column_names)
    for row in data:
        writer.writerow(row)

    return response

def query_q2(request):
    custom_query = """SELECT
    department_id,
    department,
    COUNT(id) as hired,
    array_agg(id) as list_ids,
    array_agg(name) as list_names
    FROM
        (
        SELECT 
            e.id as id,
            e.name as name,
            d.id as department_id,
            d.department as department,
            j.job as job
        FROM
            employees_data.hired_employees e
            INNER JOIN employees_data.departments d
                ON d.id = e.department_id
            INNER JOIN employees_data.jobs j
                ON j.id = e.job_id
        WHERE 
            EXTRACT(year FROM datetime) = 2021
        ) as data_joined
    GROUP BY
        department_id,
        department
    HAVING COUNT(id) > (
        SELECT AVG(count_per_department) as average
        FROM (
            SELECT 
                e.department_id,
                COUNT(e.id) as count_per_department
            FROM employees_data.hired_employees e
            WHERE EXTRACT(year FROM datetime) = 2021
            GROUP BY e.department_id
        ) as department_counts
    )
    ORDER BY
        COUNT(id) DESC    
    """

    data = []
    # Execute the custom query and fetch the data
    with connection.cursor() as cursor:
        cursor.execute(custom_query)
        column_names = [desc[0] for desc in cursor.description]
        for row in cursor:
            data.append(dict(zip(column_names, row)))

    # Paginate the results
    page_number = request.GET.get(
        "page", 1
    )  # Get the current page number from the request
    items_per_page = 20  # Number of items to display per page
    paginator = Paginator(data, items_per_page)
    page = paginator.get_page(page_number)


    return render(request, "q2.html", {"page": page, "columns": column_names})

def get_q2(request):
    custom_query = """SELECT
    department_id,
    department,
    COUNT(id) as hired,
    array_agg(id) as list_ids,
    array_agg(name) as list_names
    FROM
        (
        SELECT 
            e.id as id,
            e.name as name,
            d.id as department_id,
            d.department as department,
            j.job as job
        FROM
            employees_data.hired_employees e
            INNER JOIN employees_data.departments d
                ON d.id = e.department_id
            INNER JOIN employees_data.jobs j
                ON j.id = e.job_id
        WHERE 
            EXTRACT(year FROM datetime) = 2021
        ) as data_joined
    GROUP BY
        department_id,
        department
    HAVING COUNT(id) > (
        SELECT AVG(count_per_department) as average
        FROM (
            SELECT 
                e.department_id,
                COUNT(e.id) as count_per_department
            FROM employees_data.hired_employees e
            WHERE EXTRACT(year FROM datetime) = 2021
            GROUP BY e.department_id
        ) as department_counts
    )
    ORDER BY
        COUNT(id) DESC    
    """

    data = []
    # Execute the custom query and fetch the data
    with connection.cursor() as cursor:
        cursor.execute(custom_query)
        column_names = [desc[0] for desc in cursor.description]
        for row in cursor:
            data.append(row)

    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=q2_data.csv'
    writer = csv.writer(response)
    writer.writerow(column_names)
    for row in data:
        writer.writerow(row)

    return response
