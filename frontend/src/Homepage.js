import {useState, useEffect} from 'react';

export const Homepage = () => {
  const [movies, setMovies] = useState([])
  useEffect(() => {
    setMovies([
      {
        name: 'Billions',
        genre: 'Drama',
        starring: 'Damian Lewis, Paul Giamatt',
      },
      {
        name: 'Sarafina',
        genre: 'drama',
        starring: 'Leleti Khumalo',
      },
    ])
  }, [])
  return (
      <div className='container col-md-6 my-4'>
        <p className='md-4'>Click below button link to add a new product.</p>
        <div className='btn btn-primary btn-sm'>Add a product</div>
        <hr />

        <div>
          {movies.map((movies, index) => {
            return (
              <div className='movies'>
                <h2>{movies.name} - {movies.genre} - {movies.starring}</h2>
              </div>
            )
          })}
        </div>
      </div>
  )
}
