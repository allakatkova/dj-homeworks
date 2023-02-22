import pytest
from django.urls import reverse
from students.models import Course, Student

# Проверяем получение первого курса


@pytest.mark.django_db
def test_get_one_course(API_client, courses_factory):
    test_courses_create = courses_factory(_quantity=1)
    first_course = test_courses_create[0]
    response = API_client.get(f'/api/v1/courses/{first_course.id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == first_course.name


# Проверяем получение списка курсов


@pytest.mark.django_db
def test_get_courses_list(API_client, courses_factory):
    test_courses_create = courses_factory(_quantity=10)
    response = API_client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    for i, course in enumerate(data):
        assert course['name'] == test_courses_create[i].name


# Проверяем фильтр списка курсов по 'id'


@pytest.mark.django_db
def test_get_courses_filter_on_id(API_client, courses_factory):
    test_courses_create = courses_factory(_quantity=1)
    response = API_client.get(
        '/api/v1/courses/', {'id': test_courses_create[0].id})
    assert response.status_code == 200
    data = response.json()
    assert test_courses_create[0].id == data[0]['id']


# Проверяем фильтр курсов по 'name'


@pytest.mark.django_db
def test_get_course_filter_on_name(API_client, courses_factory):
    test_courses_create = courses_factory(_quantity=1)
    response = API_client.get(
        '/api/v1/courses/', {'name': test_courses_create[0].name})
    assert response.status_code == 200
    data = response.json()
    assert test_courses_create[0].name == data[0]['name']


# Проверяем успешность создания курса


@pytest.mark.django_db
def test_course_creation(API_client):
    response = API_client.post(reverse('courses-list'), data={
        'name': 'test_course_name'
    }, format='json')
    assert response.status_code == 201
    data = response.json()
    assert Course.objects.get(id=data['id']).name == 'test_course_name'


# Проверяем успешность обновления курса


@pytest.mark.django_db
def test_course_update(API_client, courses_factory):
    course = courses_factory()
    url = reverse('courses-detail', args=(course.id,))
    payload = {
        "name": "new course"
    }
    response = API_client.patch(url, payload, format="json")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == 'new course'


# Проверяем успешность удаления курса


@pytest.mark.django_db
def test_course_delete(API_client, courses_factory):
    test_courses_create = courses_factory(_quantity=1)
    response = API_client.delete(
        reverse('courses-detail', args=[test_courses_create[0].id]))
    assert response.status_code == 204
