#Problem 1.1 

def load_movies_dataframe(file_path):
    index = 0
    indices = []
    data = {'title': [],
            'year': [],
            'genre': []}
    cols = ['title', 'year', 'genre']
    with open (file_path) as file:
        for line in file:
            for word in line.split("|"):
                if (index == 0):
                    indices.append(int(word))
                    index = index + 1
                    continue
                if (index == 1):
                    data['title'].append(word)
                elif (index == 2):
                    data['year'].append(int(word)) #cast the string to an int cause a year is represented by a number 
                else:
                    data['genre'].append(word)
                if (index < 3):
                    index = index + 1
                else:
                    index = 0   
                    
    df = pd.DataFrame(data, index = indices, columns = cols)
    df['genre'] = df['genre'].str.replace('\n', '')
    df_sorted = df.sort_index()
    return df_sorted

    #pass

#Problem 1.2 

def load_ratings_dataframe(file_path):

    #lists for user id, movie id, and ratings to add to for each line in the CSV and move to the data frame later 
    user_id_list = []
    movie_id_list = []
    ratings_list = []
    
    #iterating through each line in the CSV, splitting it for the necessary info and adding it to the correct lists
    with open(file_path) as file: 
        for line in file: 
            user_id, movie_id, rating = line.strip().split(",")
            user_id_list.append(int(user_id))
            movie_id_list.append(int(movie_id))
            ratings_list.append(float(rating))
        
    #creating the data frame using the lists that have all the info added to them
    df = pd.DataFrame({'user_id': user_id_list, 'movie_id': movie_id_list, 'rating': ratings_list})
    
    #sort by user id
    ratings_df = df.sort_values(by = 'user_id') 
    
    return ratings_df #return the dataframe

    #pass

#Problem 1.3

def count_unique_genres(movies_df):
    """
    Counts the unique genres in the movies DataFrame.
    
    Parameters:
    movies_df (DataFrame): A pandas DataFrame containing movie data.
    
    Returns:
    int: The count of unique genres.
    """
    
    all_genres = [] #empty list to store all genres from the DataFrame 
    
    #iterate through the data frame and add all genres to the list
    for genre in movies_df['genre']: 
        all_genres.append(genre) 
        
    #set only contains unique elements so casting to a set will get rid of all duplicates 
    unique_genre = set(all_genres) 
    
    #length of the set will give you the number of unique genres in the movies DataFrame
    count = len(unique_genre) 

    return count 

   #pass

#Problem 1.4

# 1.4
def average_rating_by_genre(movies_df, ratings_df):
    """
    Calculates the average rating for each genre.
    
    Parameters:
    movies_df (DataFrame): A pandas DataFrame containing movie data, indexed by 'movie_id'.
    ratings_df (DataFrame): A pandas DataFrame containing ratings data.
    
    Returns:
    Series: A pandas Series where the index is the genre and the value is the average rating for that genre.
    """
    
    #gets the values from the genre column in the movies_df
    genres = movies_df['genre']
    
    #creates a Series to store the average rating for that genre
    avg_ratings_genre = pd.Series()

    #iterates through each genre in the genres list
    for genre in genres:
        genre_movies = movies_df[movies_df['genre'] == genre].index #gets the index value of all movies in that particular genre 
        genre_ratings = ratings_df[ratings_df['movie_id'].isin(genre_movies)]['rating'] #gets the ratings for the correct movies in that particular genre by making sure they are present in that ID
        avg_rating_genre = genre_ratings.mean() #gets the mean for all the movies in the current genre
        avg_ratings_genre[genre] = avg_rating_genre #uses the index of the genre to assign it the value of the average rating

    return avg_ratings_genre  #returns the average rating by Genre pandas series

    #pass

#Problem 1.5

def calculate_average_ratings(ratings_df):
    """
    Calculates the average rating for each movie.

    Parameters:
    ratings_df (DataFrame): DataFrame containing ratings data, with 'movie_id' and 'rating' columns.
    
    Returns:
    Series: A pandas Series where the index is 'movie_id' and the value is the average rating for each movie.
    """
    
    #groupby is used to group the ratings by 'movie_id'
    group_ratings = ratings_df.groupby('movie_id')
    
    #getting he mean for each movie in the ratings column
    avg_ratings_movie = group_ratings['rating'].mean()
    
    #avg_ratings_movie = ratings_df.groupby('movie_id')['rating'].mean()
    
    return avg_ratings_movie

    pass

#Problem 1.6

def highest_rated_movie_id_by_genre_and_year(movies_df, ratings_df, genre, year):
    """
    Finds the movie_id of the highest-rated movie for a given genre and year.
    
    Parameters:
    movies_df (DataFrame): DataFrame containing movie data.
    ratings_df (DataFrame): DataFrame containing ratings data.
    genre (str): The genre to filter movies by.
    year (int or str): The year to filter movies by.
    
    Returns:
    The `movie_id` of the highest-rated movie for the specified genre and year. Returns `None` if no movie matches the criteria.
    """ 
    
    #checks if there is a col name of movie_id 
    #if there isn't, its renaming the index column to be the movie_id and thus creates unique identifiers
    if 'movie_id' not in movies_df.columns:
        movies_df = movies_df.reset_index().rename(columns={'index': 'movie_id'})

        
    # Filters the movie based on the year and genre parameters provided as input for the function
    filtered_movies = movies_df[(movies_df['genre'] == genre) & (movies_df['year'] == year)]


    # if there is no movie fitting the genre/year criteria, then it returns None 
    if filtered_movies.empty:
        return None


    # Merges original ratings with filtered movies, keeping those data frames that have the matching movie IDs
    movie_ratings = pd.merge(filtered_movies, ratings_df, on='movie_id', how='inner')


    #Calculates the title, avg rating, and count of ratings for every movie. 
    #the resulting dataframe is set by that index
    stat_ratings = movie_ratings.groupby('movie_id').agg(
    title=pd.NamedAgg(column='title', aggfunc='first'),
    average_rating=pd.NamedAgg(column='rating', aggfunc='mean'),
    rating_count=pd.NamedAgg(column='rating', aggfunc='count') ).reset_index()

    #this sorts the dataframe such that movies that have a higher avg rating and higher count of ratings will be present first in the df 
    stat_ratings.sort_values(by=['average_rating', 'rating_count'], ascending=[False, False], inplace=True)


    #if the top movie has does not have ratings, it returns None
    if stat_ratings.iloc[0]['rating_count'] == 0:
        return None

    #if there is ratings present, this returns the movie_id of the highest rated movie
    return stat_ratings.iloc[0]['movie_id']

    pass
