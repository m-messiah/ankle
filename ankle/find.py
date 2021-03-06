import html5lib

from .utils import is_string
from .match import node_matches_bone


__all__ = ['find', 'find_all', 'find_iter']


def find(skeleton, document):
    """
    Return the first element that matches given skeleton in the document.
    """
    return next(find_iter(skeleton, document), None)


def find_all(skeleton, document):
    """
    Return all elements from document that match given skeleton.

    Skeleton elements are compared with the document's by tag name,
    attributes and text inside or between them.

    Children of elements in the skeleton are looked for in the descendants of
    matching elements in the document.

    Order of elements in the skeleton is signficant.

    Skeleton must contain one root element.

    `document` and `skeleton` may be either HTML strings or parsed etrees.
    """
    return list(find_iter(skeleton, document))


def find_iter(skeleton, document):
    """
    Return an iterator that yields elements from the document that
    match given skeleton.

    See `find_all` for details.
    """
    if is_string(document):
        document = html5lib.parse(document)
    if is_string(skeleton):
        fragment = html5lib.parseFragment(skeleton)
        if len(fragment) != 1:
            raise ValueError("Skeleton must have exactly one root element.")
        skeleton = fragment[0]

    for element in document.iter():
        if node_matches_bone(element, skeleton):
            yield element
