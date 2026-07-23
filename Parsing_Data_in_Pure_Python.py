with open("initialdata.txt", encoding="utf-8") as f:
    data = f.read()

# Har profile ko alag karo
chunks = data.split("\n\n")
chunks = [c.strip() for c in chunks if c.strip()]


# Number convert karne ka function
def convert_number(text):
    text = text.lower().replace(",", "").strip()

    if "k" in text:
        return int(float(text.replace("k", "").split()[0]) * 1000)

    elif "m" in text:
        return int(float(text.replace("m", "").split()[0]) * 1000000)

    else:
        return int("".join(ch for ch in text if ch.isdigit()))


# Ek profile parse karo
def parse_chunk(chunk):
    lines = chunk.split("\n")

    username = lines[0]

    posts = convert_number(lines[1])
    followers = convert_number(lines[2])
    following = convert_number(lines[3])

    display_name = lines[4]

    bio = "\n".join(lines[5:])

    return {
        "username": username,
        "posts": posts,
        "followers": followers,
        "following": following,
        "display_name": display_name,
        "bio": bio
    }


all_data = []

for c in chunks:
    all_data.append(parse_chunk(c))


print(all_data)


# Sabse zyada posts
max_posts = max(all_data, key=lambda x: x["posts"])

print("\nProfile with Maximum Posts")
print(max_posts)


# Sabse zyada followers
max_followers = max(all_data, key=lambda x: x["followers"])

print("\nProfile with Maximum Followers")
print(max_followers)

#max following
max_following = max(all_data, key=lambda x: x["following"])
print(max_following)

all_chunks = []

for chunk in chunks:
    parsed_chunk = parse_chunk(chunk)
    all_chunks.append(parsed_chunk)

print(all_chunks)  
  