#сделать каждое предложение текста с заглавной буквы

s = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. aenean tempus commodo diam, vel ornare tellus. morbi accumsan ante vel quam venenatis, vitae porta tortor accumsan. integer viverra lectus purus, a dignissim mi malesuada ut. in enim mi, tincidunt eu viverra quis, eleifend sed ex. nullam quam lectus, mattis quis tincidunt ut, consectetur in neque. vestibulum ultrices lacus id eros viverra dapibus. sed nisl lectus, accumsan nec vehicula nec, faucibus at nibh. proin dapibus bibendum dictum. suspendisse facilisis suscipit magna quis laoreet. sed congue, turpis a maximus cursus, odio diam laoreet magna, sed ultrices mi orci nec orci. nullam commodo aliquam rhoncus. aenean ut mi semper, pellentesque erat vitae, congue mauris. ut nec velit eleifend mi feugiat consequat id eu urna. nullam tristique ante consequat, tempor ligula nec, vestibulum ligula. duis a finibus dolor, sed rhoncus eros. ut sed diam eget sapien aliquam tincidunt in et risus. integer nibh dolor, luctus quis pharetra at, tempus eget metus. phasellus pulvinar justo ipsum, in elementum leo tristique gravida. praesent mattis nunc ac nibh vulputate cursus. praesent maximus tempor consectetur. class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. maecenas ut sem id metus faucibus ullamcorper. sed luctus orci nibh, nec consequat urna eleifend et. duis ultrices congue ex, sed elementum turpis. quisque eu augue diam. nullam molestie venenatis scelerisque. vestibulum sollicitudin orci eu eros tincidunt, ac pellentesque arcu cursus. fusce interdum neque eget nisl pulvinar lacinia. maecenas malesuada nulla vitae purus suscipit viverra. class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. nulla scelerisque sagittis consequat. maecenas arcu ante, tempor in lacus ac, convallis pulvinar lectus. pellentesque eget lacus quis nulla semper congue. suspendisse dignissim risus mi, at tincidunt mi auctor a. aenean eros lacus, mattis sit amet velit in, euismod semper justo. fusce et orci ac massa semper dictum et ac neque. phasellus ornare vehicula ultrices. proin ultricies tincidunt sapien, et laoreet libero sodales eu. ut ut elit quis velit feugiat tempor in vel neque. suspendisse tortor dui, pharetra eget nisi eu, mollis egestas dolor. morbi facilisis enim at ultricies tincidunt. cras magna erat, sollicitudin quis finibus eu, rhoncus sit amet est. praesent in interdum odio. aenean eu finibus lectus, ut tempus leo. mauris mauris elit, pretium id vulputate in, eleifend semper diam. maecenas faucibus ante eu blandit aliquam. sed blandit, felis in eleifend finibus, ipsum ipsum vulputate nunc, vel rhoncus nibh dui in nulla. orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. nunc vitae nulla porta, tempor mi vel, maximus nisl. quisque ac elit quam. phasellus ullamcorper velit ac velit hendrerit scelerisque eu ac sem. phasellus porttitor diam rutrum odio dictum vestibulum. cras tincidunt lorem ac turpis dictum, id fermentum nisl blandit. aliquam vel aliquet ipsum. in euismod, sem ut tincidunt venenatis, velit leo luctus nisi, a viverra augue nisi in tellus. nunc varius dui nisi, non ultricies felis posuere nec. aliquam vitae odio non leo sagittis fermentum vel non turpis. donec suscipit, erat at feugiat pulvinar, nisl mauris ornare metus, et mollis lacus enim ac sem. nunc finibus augue et quam bibendum semper'

def zagl(l):
    l = l.split('. ')
    for i in range(0, len(l)):
        l[i] = l[i][:1].upper() + l[i][1:] + '.'
    s2 = ' '.join(l)
    print('\nResult:\n', s2)

zagl(s)
