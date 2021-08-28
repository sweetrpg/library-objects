//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class AuthorTagPivot : Model {
    public static let schema = "author_tags"

    @ID
    public var id : UUID?

    @Parent(key: "authorId")
    public var author : Author

    @Parent(key: "tagId")
    public var tag : Tag

    public init() {}

    public init(id : UUID? = nil, author : Author, tag : Tag) throws {
        self.id = id
        self.$author.id = try author.requireID()
        self.$tag.id = try tag.requireID()
    }

}
