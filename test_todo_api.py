import requests
import pytest

endpoint = "https://todo.pixegami.io/"

def test_endpoint_url():
        endpoit_response = requests.get(endpoint)
        assert endpoit_response.status_code == 200
        return endpoint



def test_create_task():
        payload = newtask_payload()
        create_task_response = create_tesk(payload)
        assert create_task_response.status_code == 200
        data = create_task_response.json()
        print(data)

        # verify the created task ID

        task_id = data['task']['task_id']
        get_task_resp = get_task({task_id})
        assert get_task_resp.status_code == 200
        get_task_data = get_task_resp.json()
        # assert get_task_data['content'] == payload[ "content"]
        # assert get_task_data['user_id'] == payload["user_id"]

def test_update_created_task():
    # create task
    payload = newtask_payload()
    create_task_response = create_tesk()
    assert create_task_response.status_code == 200


    task_id= create_task_response.json()['task']['task_id']

     # update task
    new_pay_load = {
        "user_id": "test_user",
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True

}
    update_task_response = update_task(new_pay_load)
    assert update_task_response.status_code == 200

    # get task and validate the changes
    get_task_response = get_task({task_id})
    assert get_task_response == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_pay_load['content']
    assert get_task_data['is done'] == new_pay_load["is_done"]



def create_tesk(paylaod):
    return requests.put(endpoint + "/create-task", json=payload)


def update_task():
    return requests.put(endpoint + "/update-task", json=payload)


def get_task():
     return requests.get(endpoint, f'/get-task/{task_id}')


def newtask_payload():
        return {
  "content": "my test content",
  "user_id": "test_user",
  "task_id": "test_task-Id",
  "is_done": False
 }
