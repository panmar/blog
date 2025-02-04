Locality-sensitive hashing: MinHash
###################################
:date: 2023-07-14 21:33
:tags: algorithm

.. image:: images/cat_twins.jpeg
    :alt: two cats: one normal, one mechanical
    :class: image-process-article-image

Imagine you’re building a meme recommendation system. Users upload memes, and you are tasked to find all similar ones quickly. A meme is described by a set of features e.g. ["*sun*", "*dog*", "*car*"]. Memes are similar if they share most features:

.. code-block:: Python

    mem_1 = ["floor", "sun", "dog", "car"]      # similar
    mem_2 = ["sun", "ball", "dog", "car"]       # similar

    mem_3 = ["tree", "grass", "dog"]            # different

How would you find all similar memes?

Well, you can directly compare memes with one another. For **N** memes this leads to O(**N**\ :sup:`2`) comparisons. We can do better!

Lets think about it. If two memes share many features and we picked a random feature from them it has high chance to be present in both. If we repeat this process many times similar memes will match more often then different ones:

.. code-block:: Python

    mems = [mem_1, mem_2, mem_3]
    all_features = ["floor", "sun", "dog", "car", "ball", "tree"]

    while all_features and memes:
        f = pick_random_feature(all_features)
        similar_mems = mems.find_all(f)
        mark_similar_mems(similar_mems)
        mems.remove(similar_mems)
        all_features.remove(f)

Notice that when we actually pick a random feature, remove it from **all_features** and pick a next one, we are actually interested in some random ordering of the features. So instead of this cumbersome procedure we could just randomly *shuffle* **all_features** and process them in order:

.. code-block:: Python

    mems = [mem_1, mem_2, mem_3]
    all_features = ["floor", "sun", "dog", "car", "ball", "tree"]

    random.shuffle(all_features)
    for f in all_features:
        if not mems:
            break
        similar_mems = mems.find_all(f)
        mark_similar_mems(similar_mems)
        mems.remove(similar_mems)

Lets simplify it even more. Instead of cumbersome shuffling we could use hash function to generate ordering. In fact, we are only interested in the smallest hash of mem's feature list. A minimum hash:

.. code-block:: Python

    mems = [mem_1, mem_2, mem_3]

    min_hashes = []
    for m in mems:
        min_hash = m.find_min_hash(hash_func)
        min_hashes.append(min_hash)

    similar_groups = group_by_hash(mems, min_hashes)

If we repeat this procedure for different hashes, the most similar mems will land more frequently in the same groups.

Described algorithm is called `MinHash <https://en.wikipedia.org/wiki/MinHash>`_ and is usefull for grouping similar sets of items.