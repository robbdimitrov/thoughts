import React from 'react';

import ThoughtItem from './thoughtitem';
import './thoughtlist.scss';

function ThoughtList({posts, users}) {
  return (
    <ul className="thought-list">
      {posts.map((post) =>
        <ThoughtItem key={post.id} post={post} user={users[0]} />
      )}
    </ul>
  );
}

export default ThoughtList;
