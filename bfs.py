from collections import deque
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def bfs(facebook, name, profession):
    """
    Finding person with target profession inside social network using BFS
    :param facebook: Social network representation
    :type facebook: dict
    :param name: Parent node name
    :type name: str
    :param profession: Target profession\
    :type profession: str
    :return: str, None
    """
    verified = []
    search_queue = deque()
    search_queue += [facebook[name]['name']]
    while search_queue:
        person = search_queue.popleft()
        if person not in verified:
            verified.append(person)
            if facebook[person]['profession'] == profession:
                logging.info(
                    "Profession '%s' has been found! Parent node '%s', target node '%s'.",
                    profession,
                    name,
                    person
                )

                return person
            else:
                for friend in fb[person].get('friends', []):
                    if friend not in verified:
                        search_queue += [friend]
    logging.info("Profession %s not found for node's %s friends.", profession, name)
    return


if __name__ == "__main__":
    fb = dict()
    fb['Sam'] = {'name': 'Sam', 'profession': 'driver', 'friends': ['Ann', 'Mike', 'Peter']}
    fb['Ann'] = {'name': 'Ann', 'profession': 'lawyer', 'friends': ['Mike', 'Kate']}
    fb['Mike'] = {'name': 'Mike', 'profession': 'killer', 'friends': ['Ann']}
    fb['Peter'] = {'name': 'Peter', 'profession': 'chef'}
    fb['Kate'] = {'name': 'Kate', 'profession': 'teacher', 'friends': ['Mike', 'Chris']}
    fb['Chris'] = {'name': 'Chris', 'profession': 'scientist'}

    bfs(facebook=fb, name='Sam', profession='teacher')
