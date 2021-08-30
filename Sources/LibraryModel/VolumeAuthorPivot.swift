//
// VolumeAuthorPivot.swift
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class VolumeAuthorPivot : Model {
    public static let schema = "volume_authors"

    @ID
    public var id : UUID?

    @Parent(key: "volumeId")
    public var volume : Volume

    @Parent(key: "authorId")
    public var author : Author

    public init() {}

    public init(id : UUID? = nil, volume : Volume, author : Author) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$author.id = try author.requireID()
    }

}
