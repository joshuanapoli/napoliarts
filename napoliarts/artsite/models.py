from django.db import models

# A Season potentially reperents a chronological duration other than one of the
# four calendar seasons.
#
class Season( models.Model ):
  title = models.CharField( max_length = 255 )  # for example, 'Spring 2011'
  shown = models.BooleanField( default = True ) # true if shown on the site
  opening = models.DateField()                  # first day of the season
  closing = models.DateField()                  # last day of the season
  def __unicode__( self ):
    return self.title

class Festival( models.Model ):
  title = models.CharField( max_length = 255 )  # for example, 'DeLand Fall Arts Festival'
  shown = models.BooleanField( default = True ) # true if shown on the site
  opening = models.DateField()                  # first day of the festival
  closing = models.DateField()                  # last day of the festival
  city = models.CharField( max_length = 255 )   # for example, 'DeLand'
  state = models.CharField( max_length = 2 )    # for example, 'FL'
  season = models.ForeignKey( Season )
  def __unicode__( self ):
    return self.title

class Portfolio( models.Model ):
  title = models.CharField( max_length = 255 )    # for example, 'Current'
  shown = models.BooleanField( default = True )   # true if shown on the site
  subtitle = models.CharField( max_length = 255 ) # for example, 'recent major works'
  statement = models.TextField()                  # artist's statement
  slug = models.SlugField( max_length = 255 )     # the portfolio will be available under ROOT/slug
  prepopulated_fields = { 'slug': ( 'title' ) }
  def __unicode__( self ):
    return self.title

# A Piece of art in a Portfolio
#
class Piece( models.Model ):
  title = models.CharField( max_length = 255 )    # for example, 'Stones in Jorden'
  shown = models.BooleanField( default = True )   # true if shown on the site
  slug = models.SlugField( max_length = 255 )     # the portfolio will be available under ROOT/portfolio.slug/slug
  material = models.CharField( max_length = 255 ) # for example, '40"x60" / Acrylic on archial paper'
  thumbnail = models.FileField( max_length = 255, upload_to = 'pieces/thumbnails' )
  image = models.FileField( max_length = 255, upload_to = 'pieces/images' )
  portfolio = models.ForeignKey( Portfolio )
  prepopulated_fields = { 'slug': ( 'title' ) }
  def __unicode__( self ):
    return self.title

class Award( models.Model ):
  title = models.CharField( max_length = 255 )    # for example, 'Second in Painting'
  shown = models.BooleanField( default = True )   # true if shown on the site
  festival = models.ForeignKey( Festival )
  def __unicode__( self ):
    return self.title

class Collection( models.Model ):
  title = models.CharField( max_length = 255 )  # for example, 'Norton Gallery & School of Art'
  shown = models.BooleanField( default = True ) # true if shown on the site
  city = models.CharField( max_length = 255 )   # for example, 'DeLand'
  state = models.CharField( max_length = 2 )    # for example, 'FL'
  def __unicode__( self ):
    return self.title
  
class Grant( models.Model ):
  title = models.CharField( max_length = 255 )    # for example, 'Individual Artist Fellowship, State of Florida Cultural Affairs'
  shown = models.BooleanField( default = True )   # true if shown on the site
  date = models.DateField()
  def __unicode__( self ):
    return self.title

class Education( models.Model ):
  title = models.CharField( max_length = 255 )  # for example, 'Bachelor of Fine Arts'
  shown = models.BooleanField( default = True ) # true if shown on the site
  city = models.CharField( max_length = 255 )   # for example, 'DeLand'
  state = models.CharField( max_length = 2 )    # for example, 'FL'
  institution = models.CharField( max_length = 255 )    # for example, 'Florida State University'
  def __unicode__( self ):
    return self.title
  
class SoloExhibition( models.Model ):
  title = models.CharField( max_length = 255 )  # not used
  shown = models.BooleanField( default = True ) # true if shown on the site
  city = models.CharField( max_length = 255 )   # for example, 'DeLand'
  state = models.CharField( max_length = 2 )    # for example, 'FL'
  institution = models.CharField( max_length = 255 ) # for example, 'Atlantic Center for the Arts'
  date = models.DateField()
  def __unicode__( self ):
    return self.title

class GroupExhibition( models.Model ):
  title = models.CharField( max_length = 255 )  # not used
  shown = models.BooleanField( default = True ) # true if shown on the site
  city = models.CharField( max_length = 255 )   # for example, 'DeLand'
  state = models.CharField( max_length = 2 )    # for example, 'FL'
  institution = models.CharField( max_length = 255 ) # for example, 'Atlantic Center for the Arts'
  date = models.DateField()
  def __unicode__( self ):
    return self.title
